def novelty_score(drug_name):
    """
    Simulated novelty scoring based on known common drugs.
    Score range: 0 - 100
    """
    if not drug_name:
        return 50

    common_drugs = [
        "aspirin",
        "paracetamol",
        "acetaminophen",
        "ibuprofen",
        "metformin"
    ]

    if drug_name.lower() in common_drugs:
        return 30  # Low novelty
    else:
        return 80  # High novelty
