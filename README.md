# Mutual Fund Analytics Capstone Project

## Overview

The Mutual Fund Analytics Capstone Project is an end-to-end data analytics solution designed to analyze Indian mutual fund data using Python, SQLite, Jupyter Notebook, and Power BI.

The project performs data ingestion, cleaning, exploratory data analysis, performance measurement, risk analytics, advanced analytics, dashboard development, and reporting. Historical mutual fund datasets are combined with live NAV data fetched through MFAPI to generate actionable insights for investors and analysts.

---

## Project Objectives

The primary objectives of this project are:

* Ingest and validate multiple mutual fund datasets
* Fetch live NAV data using MFAPI
* Store and manage data using SQLite
* Perform data cleaning and quality validation
* Analyze fund performance and risk
* Calculate financial and risk-adjusted metrics
* Build interactive dashboards
* Generate reports and presentations
* Develop a simple fund recommendation engine

---

## Project Structure

```text
bluestock_mf_capstone/
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── compute_metrics.py
│   └── recommender.py
├── sql/
│   ├── schema.sql
│   └── queries.sql
├── dashboard/
│   └── bluestock_mf.pbix
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
└── README.md
```

---

## Datasets Used

The project uses the following mutual fund datasets:

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

Additional derived datasets:

* alpha_beta.csv
* fund_scorecard.csv

---

## Technology Stack

### Programming Language

* Python 3.x

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Requests
* SQLite3
* SQLAlchemy
* SciPy
* Jupyter Notebook

### Tools

* Visual Studio Code
* Git
* GitHub
* SQLite
* Power BI

---

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd bluestock_mf_capstone
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Project Workflow

### Phase 1 - Data Ingestion

* Loaded all mutual fund datasets
* Profiled datasets
* Identified missing values
* Identified duplicate records
* Validated dataset structure

Notebook:

```text
01_data_ingestion.ipynb
```

---

### Phase 2 - Data Cleaning

Performed:

* Missing value treatment
* Duplicate removal
* Data type corrections
* Date standardization
* Dataset consistency checks

Notebook:

```text
02_data_cleaning.ipynb
```

---

### Phase 3 - Exploratory Data Analysis

Analysis performed on:

* Fund categories
* Asset Management Companies (AMCs)
* Assets Under Management (AUM)
* Risk metrics
* Expense ratios
* Portfolio holdings
* SIP investments

Notebook:

```text
03_eda_analysis.ipynb
```

---

### Phase 4 - Performance Analytics

Calculated and analyzed:

* Returns
* Alpha
* Beta
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown
* Volatility
* Fund Rankings

Notebook:

```text
04_performance_analytics.ipynb
```

---

### Phase 5 - Advanced Analytics

Implemented:

* Value at Risk (VaR) Analysis
* SIP Performance Analysis
* Portfolio Concentration Analysis
* HHI (Herfindahl-Hirschman Index)
* Risk-Based Fund Recommendation Engine

Notebook:

```text
05_advanced_analytics.ipynb
```

---

## Live NAV Data Integration

Live NAV data was fetched using MFAPI.

Source:

```text
https://api.mfapi.in
```

Sample Funds:

* SBI Bluechip Fund
* ICICI Prudential Bluechip Fund
* Nippon India Large Cap Fund
* Axis Bluechip Fund
* Kotak Bluechip Fund

Stored in:

```text
data/raw/live_nav/
```

Script:

```bash
python scripts/live_nav_fetch.py
```

---

## ETL Pipeline

The ETL pipeline loads processed datasets into SQLite for reporting and dashboarding.

Run:

```bash
python scripts/etl_pipeline.py
```

Database Output:

```text
data/db/bluestock_mf.db
```

---

## Fund Recommendation Engine

The recommendation engine suggests funds based on investor risk appetite.

Supported Risk Profiles:

* Low Risk
* Moderate Risk
* High Risk

Run:

```bash
python scripts/recommender.py
```

---

## Dashboard

A Power BI dashboard was developed to visualize mutual fund analytics.

Dashboard Pages:

1. Executive Overview
2. Fund Performance Analysis
3. Risk Analytics
4. Investment Recommendations

Dashboard File:

```text
dashboard/bluestock_mf.pbix
```

---

## Reports

### Final Project Report

```text
reports/Final_Report.pdf
```

Contents:

* Executive Summary
* Data Sources
* ETL Design
* EDA Findings
* Performance Analysis
* Risk Analytics
* Dashboard Screenshots
* Recommendations

### Presentation

```text
reports/Presentation.pptx
```

Contains a 12-slide summary of the project.

---

## Key Insights

* Mutual fund performance varies significantly across categories and fund houses.
* Funds with higher Sharpe ratios generally provide superior risk-adjusted returns.
* Portfolio concentration can be measured using HHI to identify diversification levels.
* SIP investments demonstrate consistent long-term wealth creation.
* Risk metrics such as VaR and Maximum Drawdown help evaluate downside exposure.

---

## Future Enhancements

* Automated ETL scheduling
* Streamlit web application
* Portfolio optimization models
* Monte Carlo simulations
* Automated report generation
* Cloud deployment

---

## Author

Prethivraj GS

Computer Science Engineering Student

Anna University

---

## Version

Current Release:

```text
v1.0
```

---

## License

This project is developed for academic and educational purposes.
