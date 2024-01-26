import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import requests
from datetime import datetime, timedelta

def fetch_data():
    # Przykładowy kod dla API
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true"
    headers = {"Authorization": "Bearer CG-XNtTAs2nibEmDABbeYcfmitB"}
    
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Sprawdź, czy zapytanie było udane
        data = response.json()  # Przekształć dane do formatu JSON
        df = pd.DataFrame(data)  # Konwertuj do DataFrame
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()  # Lub inny sposób obsługi błędów
