import asyncio
from string import ascii_uppercase

from django.db.models import Count, Avg
from django.db import DatabaseError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import EvaluationSession, ModelResponse, JudgeScore
from .serializers import PromptInputSerializer, EvaluationSessionSerializer
from .llm_clients import fetch_all_responses
from .judge import run_judges
from .consensus import run_consensus_analysis


class EvaluateView(APIView):
    """
    POST /api/evaluate/
    Receives user prompts, executes concurrent LLM evaluations, processes consensus metrics, 
    and saves execution audit data to the primary relational store.
    """
    @swagger_auto_schema(request_body=PromptInputSerializer)
    def post(self, request):

        # ── Step 1: Input Serialization and Verification ──────
        serializer = PromptInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"error": "Invalid input.", "details": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        prompt = serializer.validated_data['prompt']

        # ── Step 2: Concurrent Non-Blocking LLM Orchestration ──
        try:
            # Executes all defined upstream LLM workers asynchronously in parallel
            llm_responses = asyncio.run(fetch_all_responses(prompt))
        except RuntimeError as e:
            return Response(
                {"error": "Async runtime error.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            return Response(
                {"error": "LLM fetch failed.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # Enforce structural checks on incoming LLM generation data
        if not llm_responses:
            return Response(
                {"error": "No LLM responses received. Check your API keys in .env file."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        # Benchmark criteria requires a minimum comparison boundary of 2 nodes
        if len(llm_responses) < 2:
            return Response(
                {
                    "error": "Only 1 model responded. Need at least 2 for evaluation.",
                    "responded": [r["model_name"] for r in llm_responses]
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        # ── Step 3: Blind Testing Anonymization Mapping ───────
        anonymized = {}
        label_map = {}
        for i, resp in enumerate(llm_responses):
            label = ascii_uppercase[i]
            anonymized[label] = resp["response_text"]
            label_map[label] = resp

        # ── Step 4: Double-Blind AI Judge Analytics ───────────
        try:
            # Dispatches masked responses to autonomous evaluator judges
            judge_results = asyncio.run(run_judges(anonymized))
        except RuntimeError as e:
            return Response(
                {"error": "Async runtime error in judge.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            return Response(
                {"error": "Judge evaluation failed.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        final_scores = judge_results.get("final_scores", {})

        # Safety fallback verification if third-party LLM evaluation fails
        if not final_scores:
            return Response(
                {"error": "Both judges failed to return scores. Check Groq and Gemini API keys."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        # ── Step 5: Statistical Consensus and Resolution ─────
        consensus_result = run_consensus_analysis(anonymized, final_scores)
        adjusted_scores = consensus_result.get("adjusted_scores", final_scores)

        # Parse target ranking profiles to dynamically resolve session winner
        pick_from = adjusted_scores if adjusted_scores else final_scores
        winner_label = max(pick_from, key=pick_from.get) if pick_from else None
        winner_model = label_map[winner_label]["model_name"] if winner_label else None
        winner_score = pick_from.get(winner_label)

        # ── Step 6: Atomic Transaction Database Commit ────────
        try:
            session = EvaluationSession.objects.create(
                prompt=prompt,
                winner_model=winner_model,
                winner_score=winner_score,
            )

            for label, resp_data in label_map.items():
                model_resp = ModelResponse.objects.create(
                    session=session,
                    model_name=resp_data["model_name"],
                    anonymous_label=label,
                    response_text=resp_data["response_text"],
                    response_time_ms=resp_data["response_time_ms"],
                    final_score=final_scores.get(label),
                )

                # Persist single granular breakdowns for auditing records
                if label in judge_results.get("groq_scores", {}):
                    JudgeScore.objects.create(
                        model_response=model_resp,
                        judge_name="Groq-Judge",
                        score=judge_results["groq_scores"][label],
                    )
                if label in judge_results.get("gemini_scores", {}):
                    JudgeScore.objects.create(
                        model_response=model_resp,
                        judge_name="Gemini-Judge",
                        score=judge_results["gemini_scores"][label],
                    )

        except DatabaseError as e:
            # Fallback handling ensuring transient storage errors do not block operational responses
            return Response(
                {
                    "warning": "Evaluation done but DB save failed.",
                    "db_error": str(e),
                    "winner": winner_model,
                    "final_score": winner_score,
                },
                status=status.HTTP_207_MULTI_STATUS
            )

        # ── Step 7: Structuring Output Response Object ────────
        result = {
            "session_id": session.id,
            "prompt": prompt,
            "winner": winner_model,
            "final_score": winner_score,
            "judges_used": {
                "groq": bool(judge_results.get("groq_scores")),
                "gemini": bool(judge_results.get("gemini_scores")),
            },
            "consensus": {
                "scores": consensus_result.get("consensus_scores", {}),
                "outliers": consensus_result.get("outliers", []),
                "confidence": consensus_result.get("confidence", "unknown"),
                "consensus_winner": consensus_result.get("consensus_winner"),
            },
            "all_responses": [
                {
                    "label": label,
                    "model_name": label_map[label]["model_name"],
                    "response_text": label_map[label]["response_text"],
                    "response_time_ms": round(label_map[label]["response_time_ms"], 2),
                    "groq_score": judge_results.get("groq_scores", {}).get(label),
                    "gemini_score": judge_results.get("gemini_scores", {}).get(label),
                    "judge_score": final_scores.get(label),
                    "consensus_score": consensus_result.get("consensus_scores", {}).get(label),
                    "adjusted_score": adjusted_scores.get(label),
                    "is_outlier": label in consensus_result.get("outliers", []),
                }
                for label in sorted(label_map.keys())
            ]
        }

        return Response(result, status=status.HTTP_200_OK)


class HistoryListView(APIView):
    """
    GET /api/history/
    Fetches past session evaluations utilizing select prefetch strategies 
    to mitigate localized ORM N+1 performance bottlenecks.
    """

    def get(self, request):
        try:
            # Optimizes query parsing by bundling foreign data connections together
            sessions = EvaluationSession.objects.prefetch_related(
                'responses__judge_scores'
            ).all()
            serializer = EvaluationSessionSerializer(sessions, many=True)
            return Response(serializer.data)
        except DatabaseError as e:
            return Response(
                {"error": "Database error.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HistoryDetailView(APIView):
    """
    GET /api/history/<id>/
    Exposes full structural details for a singular targeted Evaluation Session.
    """

    def get(self, request, pk):
        try:
            pk = int(pk)
        except (ValueError, TypeError):
            return Response(
                {"error": "Invalid session ID. Must be a number."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            session = EvaluationSession.objects.prefetch_related(
                'responses__judge_scores'
            ).get(pk=pk)
        except EvaluationSession.DoesNotExist:
            return Response(
                {"error": f"Session {pk} not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except DatabaseError as e:
            return Response(
                {"error": "Database error.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        serializer = EvaluationSessionSerializer(session)
        return Response(serializer.data)


class LeaderboardView(APIView):
    """
    GET /api/leaderboard/
    Performs on-the-fly analytical data aggregation across Model records 
    to generate real-time performance rank listings.
    """

    def get(self, request):
        try:
            # Query executes grouping and score calculations concurrently at database layer
            stats = (
                ModelResponse.objects
                .values('model_name')
                .annotate(
                    total_evaluations=Count('id'),
                    average_score=Avg('final_score'),
                )
                .order_by('-average_score')
            )

            # Map wins distribution tracking profiles independently
            wins_qs = (
                EvaluationSession.objects
                .values('winner_model')
                .annotate(wins=Count('id'))
            )
            wins_map = {w['winner_model']: w['wins'] for w in wins_qs}

            if not stats:
                return Response(
                    {"message": "No evaluations yet. Submit a prompt first."},
                    status=status.HTTP_200_OK
                )

            leaderboard = []
            for entry in stats:
                name = entry['model_name']
                leaderboard.append({
                    "model_name": name,
                    "total_wins": wins_map.get(name, 0),
                    "average_score": round(entry['average_score'] or 0, 2),
                    "total_evaluations": entry['total_evaluations'],
                })

            # Sort listings structurally using total match wins as primary key constraint
            leaderboard.sort(key=lambda x: x['total_wins'], reverse=True)
            return Response(leaderboard)

        except DatabaseError as e:
            return Response(
                {"error": "Database error.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )