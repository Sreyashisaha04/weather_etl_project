import pandas as pd
import os

def load_to_csv(df, file_path='data/weather_data.csv'):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        existing_df = pd.read_csv(file_path)
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass

    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")