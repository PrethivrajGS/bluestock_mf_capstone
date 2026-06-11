"""
ETL Pipeline for Mutual Fund Analytics Project

Loads processed datasets and stores them in SQLite.
"""

import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("../data/db/bluestock_mf.db")

print("Loading datasets...")

# Load datasets
fund_master = pd.read_csv("../data/processed/fund_master.csv")

scheme_details = pd.read_csv(
    "../data/processed/scheme_details.csv"
)

nav_history = pd.read_csv(
    "../data/processed/nav_history.csv"
)

aum_data = pd.read_csv(
    "../data/processed/aum_data.csv"
)

returns_data = pd.read_csv(
    "../data/processed/returns_data.csv"
)

risk_metrics = pd.read_csv(
    "../data/processed/risk_metrics.csv"
)

expense_ratio = pd.read_csv(
    "../data/processed/expense_ratio.csv"
)

portfolio_holdings = pd.read_csv(
    "../data/processed/portfolio_holdings.csv"
)

benchmark_data = pd.read_csv(
    "../data/processed/benchmark_data.csv"
)

sip_data = pd.read_csv(
    "../data/processed/sip_data.csv"
)

alpha_beta = pd.read_csv(
    "../data/processed/alpha_beta.csv"
)

fund_scorecard = pd.read_csv(
    "../data/processed/fund_scorecard.csv"
)

print("Datasets loaded successfully")

# Save tables into SQLite

fund_master.to_sql(
    "fund_master",
    conn,
    if_exists="replace",
    index=False
)

scheme_details.to_sql(
    "scheme_details",
    conn,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "nav_history",
    conn,
    if_exists="replace",
    index=False
)

aum_data.to_sql(
    "aum_data",
    conn,
    if_exists="replace",
    index=False
)

returns_data.to_sql(
    "returns_data",
    conn,
    if_exists="replace",
    index=False
)

risk_metrics.to_sql(
    "risk_metrics",
    conn,
    if_exists="replace",
    index=False
)

expense_ratio.to_sql(
    "expense_ratio",
    conn,
    if_exists="replace",
    index=False
)

portfolio_holdings.to_sql(
    "portfolio_holdings",
    conn,
    if_exists="replace",
    index=False
)

benchmark_data.to_sql(
    "benchmark_data",
    conn,
    if_exists="replace",
    index=False
)

sip_data.to_sql(
    "sip_data",
    conn,
    if_exists="replace",
    index=False
)

alpha_beta.to_sql(
    "alpha_beta",
    conn,
    if_exists="replace",
    index=False
)

fund_scorecard.to_sql(
    "fund_scorecard",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\nETL Pipeline Completed Successfully")
print("Database created at:")
print("../data/db/bluestock_mf.db")