"""
consensus.py — Consensus Scoring using Gemini Embeddings
Flow:
1. Har response ko Gemini API se embed karo (vector banao)
2. Cosine Similarity se compare karo (yeh same hai)
3. Outliers detect karo
4. Final adjusted score nikalo
"""

import asyncio
import numpy as np
import google.generativeai as genai
# from google import genai
# from google.genai import types
from django.conf import settings
import numpy as np
import httpx

# Step 1: Gemini se ek response ka embedding lo
def get_embedding(text: str) -> list:
    """
    OpenRouter se Gemini embedding-2 model use karo.
    TF-IDF ki jagah real semantic embeddings milti hain.
    """
    try:
        response = httpx.post(
            "https://openrouter.ai/api/v1/embeddings",
            headers={
                "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "google/gemini-embedding-2",
                "input": text,
            },
            timeout=30.0,
        )
        response.raise_for_status()
        data = response.json()
        return data["data"][0]["embedding"]

    except Exception as e:
        print(f"[Embedding Error] {e}")
        return []

# Step 2: Saare responses ke embeddings (parallel)
async def get_all_embeddings(responses: dict) -> dict:
    """
    Har response label ke liye Gemini embedding lo.
    asyncio executor use karo — genai library sync hai.

    Returns: { "A": [0.12, 0.45, ...], "B": [...], ... }
    """
    if not settings.GEMINI_API_KEY:
        print("[Consensus] GEMINI_API_KEY missing")
        return {}

    loop = asyncio.get_event_loop()
    embeddings = {}

    async def embed_one(label, text):
        try:
            vector = await loop.run_in_executor(
                None, lambda t=text: get_embedding(t)
            )
            if vector:
                embeddings[label] = vector
                print(f"[Embedding] {label} OK — {len(vector)} dims")
            else:
                print(f"[Embedding] {label} failed")
        except Exception as e:
            print(f"[Embedding] {label} error: {e}")

    await asyncio.gather(*[embed_one(l, t) for l, t in responses.items()])
    return embeddings

# Step 3: Cosine Similarity
def cosine_similarity_score(vec1: list, vec2: list) -> float:
    """
    Do vectors ka angle measure karo.
    1.0 = same meaning, 0.0 = unrelated

    Formula: cos(theta) = (A . B) / (|A| x |B|)
    """
    try:
        a = np.array(vec1)
        b = np.array(vec2)
        dot = np.dot(a, b)
        mag = np.linalg.norm(a) * np.linalg.norm(b)
        return float(dot / mag) if mag != 0 else 0.0
    except Exception as e:
        print(f"[Cosine Error] {e}")
        return 0.0

# Step 4: Similarity Matrix
def compute_similarity_matrix(embeddings: dict) -> tuple:
    """
    Har pair ke beech similarity nikalo.
    NxN matrix return karta hai.
    """
    labels = sorted(embeddings.keys())
    n = len(labels)
    if n == 0:
        return [], np.array([])
    if n == 1:
        return labels, np.ones((1, 1))

    matrix = np.zeros((n, n))
    for i, li in enumerate(labels):
        for j, lj in enumerate(labels):
            if i == j:
                matrix[i][j] = 1.0
            elif j > i:
                sim = cosine_similarity_score(embeddings[li], embeddings[lj])
                matrix[i][j] = sim
                matrix[j][i] = sim
    return labels, matrix

# Step 5: Consensus Scores
def calculate_consensus_scores(labels: list, sim_matrix: np.ndarray) -> dict:
    """Har response ka average similarity baaki sab se."""
    consensus = {}
    n = len(labels)
    for i, label in enumerate(labels):
        if n <= 1:
            consensus[label] = 1.0
            continue
        sims = [float(sim_matrix[i][j]) for j in range(n) if i != j]
        consensus[label] = round(sum(sims) / len(sims), 4) if sims else 0.0
    return consensus
# Step 6: Outlier Detection
def detect_outliers(consensus_scores: dict, threshold: float = 0.15) -> list:
    """
    Mean se 1.5 sigma neeche AND raw score < 0.15 = outlier.
    """
    if len(consensus_scores) < 3:
        return []
    scores = list(consensus_scores.values())
    mean = sum(scores) / len(scores)
    std = float(np.std(scores))
    outliers = []
    for label, score in consensus_scores.items():
        if score < (mean - 1.5 * std) and score < threshold:
            outliers.append(label)
            print(f"[Outlier] {label} — score:{score:.4f} mean:{mean:.4f}")
    return outliers

# Step 7: Score Adjustment

def adjust_scores_with_consensus(
    final_scores: dict,
    consensus_scores: dict,
    outliers: list,
    weight: float = 0.2
) -> dict:
    """
    Adjusted = (Judge x 0.80) + (Consensus x 0.20)
    Outlier penalty: consensus aur half
    """
    adjusted = {}
    for label, judge_score in final_scores.items():
        if judge_score is None:
            adjusted[label] = None
            continue
        consensus = consensus_scores.get(label, 0.5)
        if label in outliers:
            consensus = consensus * 0.5
        adj = (judge_score * (1 - weight)) + (consensus * 10 * weight)
        adjusted[label] = round(adj, 2)
    return adjusted

# ASYNC MAIN
async def run_consensus_analysis_async(responses: dict, judge_final_scores: dict) -> dict:
    """Gemini embeddings lo phir full analysis karo."""
    if not responses:
        return _empty_result(judge_final_scores)

    # Gemini embeddings
    embeddings = await get_all_embeddings(responses)

    # Kam embeddings aaye — fallback
    if len(embeddings) < 2:
        print("[Consensus] Not enough embeddings — fallback")
        eq = round(1.0 / max(len(responses), 1), 4)
        return {
            "similarity_matrix": {},
            "consensus_scores": {l: eq for l in responses},
            "outliers": [],
            "adjusted_scores": judge_final_scores,
            "consensus_winner": max(judge_final_scores, key=judge_final_scores.get) if judge_final_scores else None,
            "confidence": "low",
            "embedding_model": "gemini-text-embedding-004",
            "embeddings_successful": len(embeddings),
        }

    labels, sim_matrix = compute_similarity_matrix(embeddings)
    consensus_scores = calculate_consensus_scores(labels, sim_matrix)
    outliers = detect_outliers(consensus_scores)
    adjusted_scores = adjust_scores_with_consensus(judge_final_scores, consensus_scores, outliers)

    valid = {k: v for k, v in adjusted_scores.items() if v is not None}
    consensus_winner = max(valid, key=valid.get) if valid else None

    avg = sum(consensus_scores.values()) / len(consensus_scores) if consensus_scores else 0
    confidence = "high" if avg >= 0.6 else ("medium" if avg >= 0.3 else "low")

    sim_dict = {
        li: {lj: round(float(sim_matrix[i][j]), 4) for j, lj in enumerate(labels)}
        for i, li in enumerate(labels)
    }

    result = {
        "similarity_matrix": sim_dict,
        "consensus_scores": consensus_scores,
        "outliers": outliers,
        "adjusted_scores": adjusted_scores,
        "consensus_winner": consensus_winner,
        "confidence": confidence,
        "embedding_model": "gemini-text-embedding-004",
        "embeddings_successful": len(embeddings),
    }

    print(f"[Consensus] Scores: {consensus_scores}")
    print(f"[Consensus] Adjusted: {adjusted_scores}")
    print(f"[Consensus] Winner: {consensus_winner} | Confidence: {confidence}")
    return result

# SYNC WRAPPER — views.py se call hota hai
def run_consensus_analysis(responses: dict, judge_final_scores: dict) -> dict:
    """
    views.py asyncio.run() se call hoti hai —
    isliye nested loop avoid karne ke liye
    ThreadPoolExecutor use karta hai.
    """
    try:
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor() as pool:
            future = pool.submit(
                asyncio.run,
                run_consensus_analysis_async(responses, judge_final_scores)
            )
            return future.result(timeout=60)
    except Exception as e:
        print(f"[Consensus] Failed: {e}")
        return _empty_result(judge_final_scores)


def _empty_result(judge_final_scores: dict) -> dict:
    """Fallback jab consensus fail ho."""
    winner = max(judge_final_scores, key=judge_final_scores.get) if judge_final_scores else None
    return {
        "similarity_matrix": {},
        "consensus_scores": {},
        "outliers": [],
        "adjusted_scores": judge_final_scores,
        "consensus_winner": winner,
        "confidence": "low",
        "embedding_model": "google/gemini-embedding-2",
        "embeddings_successful": 0,
    }