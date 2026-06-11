import pandas as pd
"""
Fund Recommendation Engine.

Recommends top mutual funds based on
user risk appetite (Low, Moderate, High).
"""
risk = pd.read_csv(
    "../data/processed/risk_metrics.csv"
)

choice = "Moderate"

if choice == "Low":

    funds = risk.sort_values(
        "std_dev_3y_pct"
    ).head(3)

elif choice == "Moderate":

    funds = risk.sort_values(
        "sharpe_ratio_3y",
        ascending=False
    ).head(3)

elif choice == "High":

    funds = risk.sort_values(
        "alpha_pct",
        ascending=False
    ).head(3)

else:

    print("Invalid Risk Level")
    exit()

print("\nTop 3 Recommended Funds\n")

print(
    funds[
        [
            "scheme_name",
            "sharpe_ratio_3y",
            "alpha_pct",
            "std_dev_3y_pct"
        ]
    ]
)