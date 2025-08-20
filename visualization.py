# visualize.py

import pandas as pd
import matplotlib.pyplot as plt

def plot_weather_metrics(csv_file="data/weather_data.csv", save_path=None):
    df = pd.read_csv(csv_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    metrics = {
        "temperature_c": "Temperature (°C)",
        "humidity": "Humidity (%)",
        "wind_speed": "Wind Speed (m/s)"
    }

    plt.figure(figsize=(12, 10))

    for i, (metric, label) in enumerate(metrics.items(), 1):
        plt.subplot(len(metrics), 1, i)
        for city in df['city'].unique():
            city_data = df[df['city'] == city]
            plt.plot(city_data['timestamp'], city_data[metric], marker='o', label=city)
        plt.ylabel(label)
        plt.legend()
        plt.grid(True)
        if i == len(metrics):
            plt.xlabel("Timestamp")
        else:
            plt.xticks([])  # Hide x labels except bottom plot

    plt.suptitle("Weather Metrics Trends by City", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    if save_path:
        plt.savefig(save_path)
        print(f"📊 Plot saved as: {save_path}")

    plt.show()

if __name__ == "__main__":
    plot_weather_metrics(save_path="data/weather_metrics_trends.png")