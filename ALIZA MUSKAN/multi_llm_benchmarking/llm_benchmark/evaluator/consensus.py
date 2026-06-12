"""
consensus.py — Consensus Scoring System

Kya karta hai:
1. Har response ko TF-IDF vector mein convert karta hai
2. Cosine similarity se responses compare karta hai
3. Outlier responses detect karta hai
4. Consensus score calculate karta hai
5. Final judge score ko consensus se adjust karta hai

No external API needed — pure Python/sklearn!
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ─────────────────────────────────────────────
# Step 1: Responses ko vectors mein convert karo
# ─────────────────────────────────────────────
def compute_similarity_matrix(responses: dict) -> tuple:
    """
    TF-IDF vectorizer se responses ko numbers mein convert karo.
    Phir har response ki doosre se similarity nikalo.

    Args:
        responses: { "A": "text...", "B": "text...", ... }

    Returns:
        labels: ["A", "B", "C", ...]
        similarity_matrix: 2D array — har pair ki similarity
    """
    labels = sorted(responses.keys())
    texts = [responses[label] for label in labels]

    # Sirf 1 response hai to similarity nahi ho sakti
    if len(texts) < 2:
        return labels, np.ones((1, 1))

    try:
        # TF-IDF — words ko importance ke saath numbers mein convert
        vectorizer = TfidfVectorizer(
            stop_words='english',    # common words (the, is, are) ignore
            min_df=1,
            ngram_range=(1, 2),      # single words + 2-word phrases
        )
        tfidf_matrix = vectorizer.fit_transform(texts)

        # Cosine similarity calculate karo
        # Result: NxN matrix jahan N = number of responses
        sim_matrix = cosine_similarity(tfidf_matrix)
        return labels, sim_matrix

    except Exception as e:
        print(f"[Consensus] Similarity computation failed: {e}")
        # Fallback — sab ko equal similarity do
        n = len(labels)
        return labels, np.ones((n, n))


# ─────────────────────────────────────────────
# Step 2: Har response ka consensus score
# ─────────────────────────────────────────────
def calculate_consensus_scores(labels: list, sim_matrix: np.ndarray) -> dict:
    """
    Har response ka average similarity nikalo baaki sab se.
    Yeh "consensus score" hai — kitna agree karta hai majority se.

    High score = majority se agree (trustworthy)
    Low score  = outlier (suspicious)

    Returns: { "A": 0.85, "B": 0.90, "C": 0.12, "D": 0.88 }
    """
    consensus = {}
    n = len(labels)

    for i, label in enumerate(labels):
        if n == 1:
            consensus[label] = 1.0
            continue

        # Apne aap ko chhod ke baaki sab se average similarity
        similarities = []
        for j in range(n):
            if i != j:
                similarities.append(float(sim_matrix[i][j]))

        avg_sim = sum(similarities) / len(similarities) if similarities else 0.0
        consensus[label] = round(avg_sim, 4)

    return consensus


# ─────────────────────────────────────────────
# Step 3: Outliers detect karo
# ─────────────────────────────────────────────
def detect_outliers(consensus_scores: dict, threshold: float = 0.15) -> list:
    """
    Jo response baaki sab se bahut alag ho — wo outlier hai.

    Method:
    - Average consensus nikalo
    - Jo response average se bahut neeche ho — outlier
    - Threshold: default 0.15 (tune kar sakte ho)

    Returns: ["C"] — outlier labels ki list
    """
    if len(consensus_scores) < 3:
        # 2 responses mein outlier detect karna reliable nahi
        return []

    scores = list(consensus_scores.values())
    mean_score = sum(scores) / len(scores)
    std_score = np.std(scores)

    outliers = []
    for label, score in consensus_scores.items():
        # Mean se 1.5 standard deviation neeche = outlier
        if score < (mean_score - 1.5 * std_score) and score < threshold:
            outliers.append(label)

    return outliers


# ─────────────────────────────────────────────
# Step 4: Judge scores ko consensus se adjust karo
# ─────────────────────────────────────────────
def adjust_scores_with_consensus(
    final_scores: dict,
    consensus_scores: dict,
    outliers: list,
    weight: float = 0.2   # consensus ka kitna asar — 20%
) -> dict:
    """
    Final score = (Judge Score × 0.80) + (Consensus Bonus × 0.20)

    Outlier responses ko penalty milti hai.

    Args:
        final_scores:     { "A": 8.5, "B": 7.0, ... }  — judge scores
        consensus_scores: { "A": 0.85, "B": 0.90, ... } — similarity scores
        outliers:         ["C"]  — penalize karo
        weight:           0.2 = consensus ka 20% asar

    Returns: { "A": 8.7, "B": 7.2, ... }  — adjusted scores
    """
    adjusted = {}

    for label, judge_score in final_scores.items():
        if judge_score is None:
            adjusted[label] = None
            continue

        consensus = consensus_scores.get(label, 0.5)

        # Outlier ko penalty
        if label in outliers:
            consensus = consensus * 0.5   # score aur kam karo

        # Consensus score 0-1 hai, judge score 0-10 hai
        # Consensus ko 0-10 scale pe lao
        consensus_scaled = consensus * 10

        # Weighted average
        adjusted_score = (judge_score * (1 - weight)) + (consensus_scaled * weight)
        adjusted[label] = round(adjusted_score, 2)

    return adjusted


# ─────────────────────────────────────────────
# Main Function — Sab ek jagah
# ─────────────────────────────────────────────
def run_consensus_analysis(responses: dict, judge_final_scores: dict) -> dict:
    """
    Poora consensus pipeline chalao.

    Args:
        responses:          { "A": "response text", ... }
        judge_final_scores: { "A": 8.5, "B": 7.0, ... }

    Returns:
    {
        "similarity_matrix":  { "A": {"A": 1.0, "B": 0.85, ...}, ... },
        "consensus_scores":   { "A": 0.85, "B": 0.90, "C": 0.12 },
        "outliers":           ["C"],
        "adjusted_scores":    { "A": 8.7, "B": 7.2, "C": 5.1 },
        "consensus_winner":   "A",
        "confidence":         "high"  / "medium" / "low"
    }
    """
    # Edge case: responses nahi hain
    if not responses:
        return {
            "similarity_matrix": {},
            "consensus_scores": {},
            "outliers": [],
            "adjusted_scores": judge_final_scores,
            "consensus_winner": max(judge_final_scores, key=judge_final_scores.get) if judge_final_scores else None,
            "confidence": "low"
        }

    # Step 1: Similarity matrix
    labels, sim_matrix = compute_similarity_matrix(responses)

    # Step 2: Consensus scores
    consensus_scores = calculate_consensus_scores(labels, sim_matrix)

    # Step 3: Outliers
    outliers = detect_outliers(consensus_scores)
    if outliers:
        print(f"[Consensus] Outliers detected: {outliers}")

    # Step 4: Adjusted scores
    adjusted_scores = adjust_scores_with_consensus(
        judge_final_scores,
        consensus_scores,
        outliers
    )

    # Step 5: Consensus winner
    valid_adjusted = {k: v for k, v in adjusted_scores.items() if v is not None}
    consensus_winner = max(valid_adjusted, key=valid_adjusted.get) if valid_adjusted else None

    # Step 6: Confidence level
    # Average consensus score kitna hai — high = sab agree, low = sab alag
    if consensus_scores:
        avg_consensus = sum(consensus_scores.values()) / len(consensus_scores)
        if avg_consensus >= 0.6:
            confidence = "high"    # sab responses similar hain
        elif avg_consensus >= 0.3:
            confidence = "medium"
        else:
            confidence = "low"     # responses bahut alag hain
    else:
        confidence = "low"

    # Similarity matrix ko readable format mein convert karo
    sim_dict = {}
    for i, label_i in enumerate(labels):
        sim_dict[label_i] = {}
        for j, label_j in enumerate(labels):
            sim_dict[label_i][label_j] = round(float(sim_matrix[i][j]), 4)

    result = {
        "similarity_matrix": sim_dict,
        "consensus_scores": consensus_scores,
        "outliers": outliers,
        "adjusted_scores": adjusted_scores,
        "consensus_winner": consensus_winner,
        "confidence": confidence,
    }

    print(f"[Consensus] Scores: {consensus_scores}")
    print(f"[Consensus] Adjusted: {adjusted_scores}")
    print(f"[Consensus] Winner: {consensus_winner} | Confidence: {confidence}")

    return result