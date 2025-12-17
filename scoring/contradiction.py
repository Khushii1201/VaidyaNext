def contradiction_score(papers):
    """
    Detects contradictory outcomes in research papers.
    Higher score = higher contradiction.
    Score range: 0 - 100
    """
    positive = 0
    negative = 0

    for paper in papers:
        text = paper.lower()

        if "improved" in text or "effective" in text or "significant benefit" in text:
            positive += 1

        if "no effect" in text or "ineffective" in text or "not significant" in text:
            negative += 1

    if positive > 0 and negative > 0:
        return 70   # High contradiction
    elif positive > 0 or negative > 0:
        return 30   # Some disagreement
    else:
        return 10   # Low contradiction
