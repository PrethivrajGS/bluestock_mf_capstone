# Mutual Fund Analytics Capstone Project

## Overview

This project is a comprehensive Mutual Fund Analytics platform designed to perform data ingestion, validation, exploratory data analysis (EDA), performance measurement, risk analytics, and dashboard reporting using Indian Mutual Fund data.

The project combines historical mutual fund datasets with live NAV data fetched from the MFAPI service to generate meaningful insights for investors and analysts.

---

## Project Objectives

* Ingest and validate multiple mutual fund datasets
* Fetch live NAV data using MFAPI
* Store and manage data efficiently
* Perform data quality checks
* Analyze fund performance and risk
* Calculate financial metrics
* Build interactive dashboards
* Generate business reports and presentations

---

## Project Structure

```text
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── db/
│   └── raw/live_nav/
│
├── notebooks/
│
├── scripts/
│
├── sql/
│
├── dashboard/
│
├── reports/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Datasets Used

The project uses 10 mutual fund datasets:

1. fund_master.csv
2. scheme_details.csv
3. nav_history.csv
4. aum_data.csv
5. returns_data.csv
6. risk_metrics.csv
7. expense_ratio.csv
8. portfolio_holdings.csv
9. benchmark_data.csv
10. sip_data.csv

---

## Technologies Used

### Programming

* Python 3.x

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLAlchemy
* Requests
* SciPy
* Jupyter Notebook

### Tools

* Visual Studio Code
* Git
* GitHub
* SQLite
* Power BI (Dashboard)

---

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd bluestock_mf_capstone
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Day 1 Deliverables

### Data Ingestion

* Project folder structure created
* Dependencies installed
* 10 CSV datasets loaded
* Dataset profiling completed
* Missing values identified
* Duplicate rows identified

### Live NAV Fetching

Live NAV data fetched from:

```text
https://api.mfapi.in
```

Funds Downloaded:

* SBI Bluechip Fund
* ICICI Bluechip Fund
* Nippon Large Cap Fund
* Axis Bluechip Fund
* Kotak Bluechip Fund

Stored in:

```text
data/raw/live_nav/
```

---

## Scripts

### data_ingestion.py

Functions:

* Load all CSV files
* Display dataset shape
* Display column names
* Display data types
* Display sample records
* Check missing values
* Check duplicate records

Run:

```bash
python scripts/data_ingestion.py
```

---

### live_nav_fetch.py

Functions:

* Connect to MFAPI
* Download historical NAV data
* Save NAV data as CSV files

Run:

```bash
python scripts/live_nav_fetch.py
```

---

## Data Quality Checks

The following validations are performed:

* Missing Value Analysis
* Duplicate Record Detection
* Data Type Validation
* AMFI Scheme Code Validation
* Dataset Relationship Verification

---

## Planned Analytics

### Exploratory Data Analysis (EDA)

* Fund category analysis
* Fund house analysis
* NAV trend analysis
* AUM analysis
* Expense ratio analysis

### Performance Metrics

* CAGR
* Annualized Return
* Volatility
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Value at Risk (VaR)

### Advanced Analytics

* Fund Recommendation Engine
* Risk Segmentation
* Portfolio Analytics
* Cohort Analysis

---

## Dashboard

Interactive dashboard pages:

1. Executive Overview
2. Fund Performance Analysis
3. Risk Analytics
4. Investment Recommendations

Tools:

* Power BI

---

## Bonus Features

* Automated NAV ETL Scheduling
* Streamlit Web Application
* Monte Carlo Simulation
* Markowitz Portfolio Optimization
* Automated Email Reporting

---

## Author

Prethivraj GS

Computer Science Engineering Student

Anna University

---

## License

This project is developed for academic and learning purposes.
