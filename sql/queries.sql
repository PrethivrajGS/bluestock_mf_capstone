-- Top 5 Funds by AUM

SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- Average NAV Per Month

SELECT
strftime('%Y-%m',full_date),
AVG(nav)
FROM fact_nav
JOIN dim_date
ON fact_nav.date_id=dim_date.date_id
GROUP BY 1;

-- SIP YoY Growth

SELECT year,
SUM(amount)
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY year;

-- Transactions By State

SELECT investor_state,
COUNT(*)
FROM fact_transactions
GROUP BY investor_state;

-- Expense Ratio Below 1%

SELECT *
FROM fact_performance
WHERE expense_ratio < 1;

-- Highest Sharpe Ratio

SELECT *
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- Lowest Beta

SELECT *
FROM fact_performance
ORDER BY beta ASC
LIMIT 10;

-- Top NAV Funds

SELECT *
FROM fact_nav
ORDER BY nav DESC
LIMIT 10;

-- Category Wise Fund Count

SELECT category,
COUNT(*)
FROM dim_fund
GROUP BY category;

-- Risk Grade Distribution

SELECT risk_grade,
COUNT(*)
FROM dim_fund
GROUP BY risk_grade;
