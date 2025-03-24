import requests

def fetch_sensor_data(sensor_id, api_key):
    url = f"https://api.purpleair.com/v1/sensors/{sensor_id}"
    headers = {"X-API-Key": api_key}
    response = requests.get(url, headers=headers)
    print(f"Sensor {sensor_id} response:", response.json())  # Add this line to debug
    return response.json()

