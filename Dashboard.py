import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import requests
from datetime import datetime, timedelta

def fetch_data():
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true"
    headers = {"Authorization": "Bearer CG-XNtTAs2nibEmDABbeYcfmitB"}
    
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  
        data = response.json()  
        df = pd.DataFrame(data) 
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()  
