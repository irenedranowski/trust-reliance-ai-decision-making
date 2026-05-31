import pandas as pd
import numpy as np

np.random.seed(42)

conditions = {
    "transparent_explanation": {
        "baseline_mean": 5.5,
        "trust_mean": 6.2,
        "reliance_mean": 5.0,
        "transparency_mean": 6.3,
        "ux_mean": 5.4,
        "follow_prob": 0.75,
        "confidence_mean": 5.2,
    },
    "high_confidence": {
        "baseline_mean": 5.0,
        "trust_mean": 5.0,
        "reliance_mean": 6.3,
        "transparency_mean": 4.0,
        "ux_mean": 5.1,
        "follow_prob": 0.80,
        "confidence_mean": 6.2,
    },
    "uncertainty_calibrated": {
        "baseline_mean": 5.0,
        "trust_mean": 4.8,
        "reliance_mean": 4.8,
        "transparency_mean": 5.0,
        "ux_mean": 5.0,
        "follow_prob": 0.55,
        "confidence_mean": 5.0,
    },
    "minimal_explanation": {
        "baseline_mean": 4.0,
        "trust_mean": 3.4,
        "reliance_mean": 3.9,
        "transparency_mean": 2.7,
        "ux_mean": 4.1,
        "follow_prob": 0.40,
        "confidence_mean": 3.8,
    },
}

def sample_rating(mean):
    value = np.random.normal(loc=mean, scale=0.8)
    return int(np.clip(np.round(value), 1, 7))

def sample_followed(prob):
    return np.random.choice(["yes", "no"], p=[prob, 1 - prob])

rows = []
n_rows = 200
condition_names = list(conditions.keys())

for _ in range(n_rows):
    condition = np.random.choice(condition_names)
    means = conditions[condition]

    rows.append({
        "condition": condition,
        "baseline_ai_trust": sample_rating(means["baseline_mean"]),
        "trust_score": sample_rating(means["trust_mean"]),
        "reliance_score": sample_rating(means["reliance_mean"]),
        "transparency_score": sample_rating(means["transparency_mean"]),
        "ux_score": sample_rating(means["ux_mean"]),
        "followed_ai": sample_followed(means["follow_prob"]),
        "decision_confidence": sample_rating(means["confidence_mean"]),
    })

df = pd.DataFrame(rows)
df.to_csv("synthetic_data.csv", index=False)