# ==========================================
# STEP 5: LOAD CLEANED DATA INTO SQLITE
# ==========================================

from sqlalchemy import create_engine, text
import pandas as pd
from pathlib import Path

# ------------------------------------------
# Create Database Folder
# ------------------------------------------

db_folder = Path("../data/db")
db_folder.mkdir(parents=True, exist_ok=True)

# ------------------------------------------
# Create SQLite Engine
# ------------------------------------------

engine = create_engine(
    "sqlite:///../data/db/bluestock_mf.db"
)

print("=" * 60)
print("LOADING CLEANED DATA INTO SQLITE")
print("=" * 60)

# ==========================================
# LOAD DIMENSION TABLES
# ==========================================

# ------------------------------------------
# DIM_FUND
# ------------------------------------------

fund_master = pd.read_csv(
    "../data/processed/fund_master.csv"
)

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded: dim_fund")

# ------------------------------------------
# DIM_DATE FROM NAV HISTORY
# ------------------------------------------

nav = pd.read_csv(
    "../data/processed/nav_history.csv"
)

nav["date"] = pd.to_datetime(nav["date"])

dim_date = pd.DataFrame({
    "full_date": nav["date"].drop_duplicates()
})

dim_date = dim_date.sort_values("full_date")

dim_date["date_id"] = range(
    1,
    len(dim_date) + 1
)

dim_date["day"] = dim_date["full_date"].dt.day
dim_date["month"] = dim_date["full_date"].dt.month
dim_date["quarter"] = dim_date["full_date"].dt.quarter
dim_date["year"] = dim_date["full_date"].dt.year

dim_date.to_sql(
    "dim_date",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded: dim_date")

# ==========================================
# LOAD FACT TABLES
# ==========================================

# ------------------------------------------
# FACT_NAV
# ------------------------------------------

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded: fact_nav")

# ------------------------------------------
# FACT_SIP
# ------------------------------------------

sip = pd.read_csv(
    "../data/processed/sip_data.csv"
)

sip.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded: fact_transactions")

# ------------------------------------------
# FACT_RETURNS
# ------------------------------------------

returns = pd.read_csv(
    "../data/processed/returns_data.csv"
)

returns.to_sql(
    "fact_returns",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded: fact_returns")

# ------------------------------------------
# FACT_RISK
# ------------------------------------------

risk = pd.read_csv(
    "../data/processed/risk_metrics.csv"
)

risk.to_sql(
    "fact_risk_metrics",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded: fact_risk_metrics")

# ------------------------------------------
# FACT_EXPENSE
# ------------------------------------------

expense = pd.read_csv(
    "../data/processed/expense_ratio.csv"
)

expense.to_sql(
    "fact_expense_ratio",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded: fact_expense_ratio")

# ------------------------------------------
# FACT_AUM
# ------------------------------------------

aum = pd.read_csv(
    "../data/processed/aum_data.csv"
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded: fact_aum")

# ------------------------------------------
# FACT_PORTFOLIO
# ------------------------------------------

portfolio = pd.read_csv(
    "../data/processed/portfolio_holdings.csv"
)

portfolio.to_sql(
    "fact_portfolio",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded: fact_portfolio")

# ------------------------------------------
# FACT_BENCHMARK
# ------------------------------------------

benchmark = pd.read_csv(
    "../data/processed/benchmark_data.csv"
)

benchmark.to_sql(
    "fact_benchmark",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded: fact_benchmark")

# ==========================================
# VERIFY ROW COUNTS
# ==========================================

print("\n" + "=" * 60)
print("ROW COUNT VALIDATION")
print("=" * 60)

tables = [
    "dim_fund",
    "dim_date",
    "fact_nav",
    "fact_transactions",
    "fact_returns",
    "fact_risk_metrics",
    "fact_expense_ratio",
    "fact_aum",
    "fact_portfolio",
    "fact_benchmark"
]

with engine.connect() as conn:

    for table in tables:

        result = conn.execute(
            text(f"SELECT COUNT(*) FROM {table}")
        )

        count = result.scalar()

        print(f"{table:<25} {count:,}")

print("\nDatabase Created Successfully!")
print("Location: data/db/bluestock_mf.db")