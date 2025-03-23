from prefect import flow, task
from sensor_monitoring.fetch import fetch_sensor_data
from sensor_monitoring.check_status import is_sensor_offline
from sensor_monitoring.notify import send_email_alert
from sensor_monitoring.logger import log_offline_sensors
from dotenv import load_dotenv
import os
import psycopg2
import yaml

load_dotenv()
db_url = os.getenv("DATABASE_URL")

conn = psycopg2.connect(db_url)

# Load sensor IDs and API key from configuration file
with open('config/sensors.yaml', 'r') as file:
    config = yaml.safe_load(file)

sensor_ids = [sensor['id'] for sensor in config['sensors']]
api_key = config['api_key']

@task
def check_sensors(sensor_ids, api_key):
    offline = []
    for sid in sensor_ids:
        data = fetch_sensor_data(sid, api_key)
        last_seen = data["sensor"]["last_seen"]
        if is_sensor_offline(last_seen):
            offline.append(sid)
    return offline

@flow
def sensor_monitoring_flow():
    offline = check_sensors(sensor_ids, api_key)
    if offline:
        send_email_alert(offline)
        
        log_offline_sensors(offline, conn_params={"dbname": "aqi_db", "user": "admin", "password": "yourpassword"})

sensor_monitoring_flow()