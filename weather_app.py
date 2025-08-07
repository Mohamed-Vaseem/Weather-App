import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "YOUR_API_KEY"  # Replace this with your real API key

def get_weather():
    city = city_entry.get().strip()

    if city.lower() in ["", "enter city"]:
        messagebox.showwarning("Invalid Input", "Please enter a valid city name.")
        return

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            result = (
                f"Weather in {data['name']}:\n"
                f"🌡️ Temperature: {data['main']['temp']}°C\n"
                f"💧 Humidity: {data['main']['humidity']}%\n"
                f"🌥️ Condition: {data['weather'][0]['description'].capitalize()}"
            )
            output_label.config(text=result)
        else:
            messagebox.showerror("Error", f"City not found: {data.get('message', '')}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Weather App 🌦️")
root.geometry("350x250")
root.resizable(False, False)

city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)
city_entry.insert(0, "")

get_button = tk.Button(root, text="Get Weather", command=get_weather)
get_button.pack(pady=10)

output_label = tk.Label(root, text="", justify="left", font=("Arial", 10))
output_label.pack(pady=10)

root.mainloop()
