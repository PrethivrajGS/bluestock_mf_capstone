"""
Compute Mutual Fund Performance Metrics.

Calculates basic performance and risk metrics
from processed mutual fund datasets.
"""

import pandas as pd

print("Loading datasets...")

returns = pd.read_csv("../data/processed/returns_data.csv")
risk = pd.read_csv("../data/processed/risk_metrics.csv")

print("Computing metrics...")

# Merge datasets
metrics = pd.merge(
    returns,
    risk,
    on=["scheme_code", "scheme_name", "amc_name"],
    how="inner"
)

# Risk-adjusted return
metrics["risk_adjusted_return"] = (
    metrics["return_1y_pct"] /
    metrics["std_dev_1y_pct"]
)

# Alpha-Beta Score
metrics["alpha_beta_score"] = (
    metrics["alpha_pct"] -
    metrics["beta"]
)

# Overall Performance Score
metrics["performance_score"] = (
    metrics["return_1y_pct"] * 0.40 +
    metrics["sharpe_ratio_1y"] * 0.30 +
    metrics["alpha_pct"] * 0.20 -
    metrics["max_drawdown_pct"] * 0.10
)

# Rank Funds
metrics["performance_rank"] = (
    metrics["performance_score"]
    .rank(ascending=False)
)

# Top funds
top_funds = metrics.sort_values(
    "performance_score",
    ascending=False
)

# Save output
top_funds.to_csv(
    "../data/processed/fund_scorecard_generated.csv",
    index=False
)

print("Metrics Computed Successfully")
print(
    "Output saved to: "
    "../data/processed/fund_scorecard_generated.csv"
)