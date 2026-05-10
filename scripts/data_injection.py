import pandas as pd
import requests
from sqlalchemy import create_engine

class DataInjection:
    def __init__(self, db_url=None):
        self.engine = create_engine(db_url) if db_url else None 

    def load_csv(self, file_path):
        try:
            df = pd.read_csv(file_path)
            print("CSV loaded successfully")
            return df
        except Exception as e:
            print(f"Error loading CSV: {e}")

    def load_excel(self, file_path):
        try:
            df = pd.read_excel(file_path)
            print("Excel loaded successfully")
            return df
        except Exception as e:
            print(f"Error loading Excel: {e}")

    def fetch_from_api(self, api_url):
        response = requests.get(api_url, timeout=30)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        print("Data from API successful")
        return df
