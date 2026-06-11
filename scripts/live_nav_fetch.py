import requests
import pandas as pd
from pathlib import Path
"""
Live NAV Fetch Module.

Fetches mutual fund NAV data from the MFAPI service
and stores the data as CSV files for further analysis.
"""
funds = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

save_path = Path("../data/raw/live_nav")
save_path.mkdir(exist_ok=True)

for fund_name, scheme_code in funds.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    file_name = save_path / f"{fund_name}.csv"

    df.to_csv(file_name, index=False)

    print(f"Saved: {file_name}")