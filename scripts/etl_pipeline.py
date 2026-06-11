import pandas as pd
import sqlite3

# Load cleaned CSVs
aum = pd.read_csv("data/processed/aum.csv")
sip = pd.read_csv("data/processed/sip.csv")
folios = pd.read_csv("data/processed/folios.csv")
schemes = pd.read_csv("data/processed/schemes.csv")

# Save into SQLite
conn = sqlite3.connect("data/db/bluestock_mf.db")
aum.to_sql("aum", conn, if_exists="replace", index=False)
sip.to_sql("sip", conn, if_exists="replace", index=False)
folios.to_sql("folios", conn, if_exists="replace", index=False)
schemes.to_sql("schemes", conn, if_exists="replace", index=False)
