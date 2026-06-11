CREATE TABLE dim_fund (
fund_id INTEGER PRIMARY KEY,
amfi_code INTEGER UNIQUE,
fund_name TEXT,
fund_house TEXT,
category TEXT,
sub_category TEXT,
risk_grade TEXT
);

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY,
full_date DATE,
day INTEGER,
month INTEGER,
quarter INTEGER,
year INTEGER
);

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY,
fund_id INTEGER,
date_id INTEGER,
nav REAL,
FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_transactions (
transaction_id INTEGER PRIMARY KEY,
fund_id INTEGER,
date_id INTEGER,
transaction_type TEXT,
amount REAL,
investor_state TEXT,
FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_performance (
performance_id INTEGER PRIMARY KEY,
fund_id INTEGER,
return_1y REAL,
return_3y REAL,
return_5y REAL,
expense_ratio REAL,
sharpe_ratio REAL,
beta REAL,
FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id)
);

CREATE TABLE fact_aum (
aum_id INTEGER PRIMARY KEY,
fund_id INTEGER,
date_id INTEGER,
aum REAL,
FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);
-- sql/schema.sql
ALTER TABLE fund_performance
ADD FOREIGN KEY (amfi_code) REFERENCES schemes(amfi_code);

ALTER TABLE sip_inflows
ADD FOREIGN KEY (date) REFERENCES aum(date);
