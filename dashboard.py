# dashboard.py

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

@st.cache_data
def load_data(csv_file="data/weather_data.csv"):
    df = pd.read_csv(csv_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def plot_metric(df, metric, label):
    plt.figure(figsize=(10,4))
    for city in df['city'].unique():
        city_data = df[df['city'] == city]
        plt.plot(city_data['timestamp'], city_data[metric], marker='o', label=city)
    plt.title(label)
    plt.xlabel("Timestamp")
    plt.ylabel(label)
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(plt)
    plt.clf()

def main():
    st.title("🌤 Weather Data Dashboard")

    df = load_data()

    st.write("### Temperature Trends")
    plot_metric(df, "temperature_c", "Temperature (°C)")

    st.write("### Humidity Trends")
    plot_metric(df, "humidity", "Humidity (%)")

    st.write("### Wind Speed Trends")
    plot_metric(df, "wind_speed", "Wind Speed (m/s)")

if __name__ == "__main__":
    main()