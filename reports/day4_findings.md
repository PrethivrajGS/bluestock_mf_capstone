# Day 4 – Performance Analytics Findings

## Overview

The objective of Day 4 was to evaluate mutual fund performance using return-based, risk-adjusted, and benchmark-relative metrics. Key measures such as CAGR, Sharpe Ratio, Sortino Ratio, Alpha, Beta, Maximum Drawdown, and a Composite Fund Scorecard were computed for all schemes.

---

## Finding 1: Daily Returns Follow a Reasonable Distribution

The distribution of daily returns across schemes was centered around zero with most observations falling within a narrow range. Extreme positive and negative returns were relatively rare, indicating stable market behavior over the analysis period.

---

## Finding 2: Long-Term CAGR Differs Significantly Across Funds

The 1-year, 3-year, and 5-year CAGR calculations revealed notable differences in long-term growth potential. Some funds consistently generated superior annualized returns compared to their peers.

**Reference:** CAGR Comparison Table

---

## Finding 3: Top Funds Deliver Better Risk-Adjusted Returns

Sharpe Ratio analysis showed that certain schemes generated significantly higher excess returns per unit of risk, making them more attractive from a portfolio perspective.

**Reference:** Sharpe Ratio Ranking

---

## Finding 4: Downside Risk Is Lower Than Total Volatility

Sortino Ratios were generally higher than Sharpe Ratios, suggesting that a considerable portion of volatility originated from positive return movements rather than losses.

**Reference:** Sortino Ratio Results

---

## Finding 5: Positive Alpha Indicates Active Management Success

Several schemes generated positive alpha values, meaning they outperformed what would be expected based on their market exposure alone.

**Reference:** alpha_beta.csv

---

## Finding 6: Market Sensitivity Varies Across Funds

Beta values showed that some schemes were more sensitive to market movements than others. High-beta funds amplified market gains and losses, while low-beta funds offered relatively stable performance.

**Reference:** Beta Analysis

---

## Finding 7: Maximum Drawdown Highlights Downside Protection

Maximum Drawdown calculations identified the largest peak-to-trough declines experienced by each fund. Funds with lower drawdowns demonstrated stronger capital preservation characteristics.

**Reference:** Drawdown Summary

---

## Finding 8: Expense Ratios Affect Overall Fund Quality

Lower expense ratio funds generally achieved better composite scores because lower costs improve investor returns over long investment horizons.

**Reference:** Expense Ratio Analysis

---

## Finding 9: Top-Ranked Funds Outperformed Benchmarks

Benchmark comparison against Nifty 50 and Nifty 100 showed that several leading funds consistently delivered superior performance over the selected evaluation period.

**Reference:** benchmark_comparison.png

---

## Finding 10: Composite Scorecard Enables Objective Ranking

The Fund Scorecard combined return, risk, alpha generation, drawdown control, and expense efficiency into a single score. This provided a balanced method for ranking all schemes on a scale of 0–100.

**Reference:** fund_scorecard.csv

---

# Metrics Computed

### Return Metrics

* Daily Returns
* 1-Year CAGR
* 3-Year CAGR
* 5-Year CAGR

### Risk Metrics

* Sharpe Ratio
* Sortino Ratio
* Beta
* Maximum Drawdown

### Benchmark Metrics

* Alpha
* Benchmark Comparison
* Tracking Error

### Composite Metric

* Fund Scorecard (0–100)

---

# Deliverables Generated

### Notebook

* Performance_Analytics.ipynb

### CSV Files

* fund_scorecard.csv
* alpha_beta.csv

### Charts

* benchmark_comparison.png

---

# Conclusion

The performance analytics phase provided a comprehensive assessment of mutual fund schemes using both return-based and risk-adjusted measures. The analysis identified top-performing funds, quantified downside risk, measured benchmark outperformance, and established a composite scoring framework for objective comparison. These results form the foundation for advanced analytics, portfolio optimization, and dashboard development in the next stages of the project.
