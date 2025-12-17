def evidence_quality_score(papers):
    """
    Calculates evidence quality score based on
    study design and strength indicators.
    Score range: 0 - 100
    """
    score = 0

    for paper in papers:
        text = paper.lower()

        if "randomized" in text or "meta-analysis" in text:
            score += 30

        if "double blind" in text:
            score += 25

        if "patients" in text or "sample size" in text:
            score += 20

        if "controlled trial" in text:
            score += 15

    return min(score, 100)
