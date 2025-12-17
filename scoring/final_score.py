def final_confidence(evidence, contradiction, novelty, market):
    """
    Combines all component scores into final confidence score.
    """
    final_score = (
        0.4 * evidence +
        0.25 * (100 - contradiction) +
        0.2 * novelty +
        0.15 * market
    )

    return round(final_score, 2)
