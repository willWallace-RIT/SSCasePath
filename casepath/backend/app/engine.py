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
def compute_intervention_scores(profile):
    urgency = 0
    instability = 0
    skill_deficit = 0
    system_fit_gap = profile.get("system_fit_gap", 0.5)

    if profile["housing_status"] == "homeless":
        urgency += 0.8
        instability += 0.7

    if profile["income"] == "none":
        urgency += 0.5
        skill_deficit += 0.3

    if profile.get("mental_health_risk"):
        urgency += 0.6
        instability += 0.5

    return {
        "urgency": urgency,
        "instability": instability,
        "skill_deficit": skill_deficit,
        "system_fit_gap": system_fit_gap
    }

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
