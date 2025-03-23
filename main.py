from prefect import flow, task
from sensor_monitoring.fetch import fetch_sensor_data
from sensor_monitoring.check_status import is_sensor_offline
from sensor_monitoring.notify import send_email_alert, send_slack_alert
from sensor_monitoring.logger import log_offline_sensors

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
    sensor_ids = [12345, 67890]  # or load from config
    api_key = "YOUR_API_KEY"
    offline = check_sensors(sensor_ids, api_key)
    if offline:
        send_email_alert(offline)
        send_slack_alert(offline)
        log_offline_sensors(offline, conn_params={"dbname": "aqi_db", "user": "admin", "password": "yourpassword"})

sensor_monitoring_flow()
