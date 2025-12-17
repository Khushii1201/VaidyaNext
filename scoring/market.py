def market_need_score(disease):
    """
    Estimates market need based on disease burden.
    Score range: 0 - 100
    """
    if not disease:
        return 50

    high_need = [
        "alzheimer",
        "cancer",
        "parkinson",
        "diabetes",
        "cardiovascular"
    ]

    if disease.lower() in high_need:
        return 85
    else:
        return 55
