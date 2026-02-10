import pandas as pd
from config import SPREADSHEET_ID

def load_google_sheet():
    url = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format=csv"
    df = pd.read_csv(url)
    return df
