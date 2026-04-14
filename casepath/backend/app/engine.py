def classify_case(profile):
    score = 0

    if profile.housing_status == "homeless":
        score += 50
    if profile.employment_status == "unemployed":
        score += 20
    if profile.mental_health_risk:
        score += 30

    if score >= 80:
        return "EMERGENCY"
    elif score >= 50:
        return "HIGH_NEED"
    elif score >= 20:
        return "MODERATE"
    return "STABLE"


def estimate_cost(classification):
    mapping = {
        "EMERGENCY": 2000,
        "HIGH_NEED": 1200,
        "MODERATE": 500,
        "STABLE": 100
    }
    return mapping.get(classification, 0)


def recommend_services(classification):
    if classification == "EMERGENCY":
        return ["Emergency Shelter", "Crisis Counseling", "Food Assistance"]
    if classification == "HIGH_NEED":
        return ["Housing Support", "Job Placement"]
    if classification == "MODERATE":
        return ["Training Programs"]
    return ["Monitoring Only"]
