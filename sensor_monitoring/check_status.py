from datetime import datetime, timedelta

def is_sensor_offline(last_seen_timestamp, threshold_hours=24):
    now = datetime.utcnow()
    last_seen = datetime.utcfromtimestamp(last_seen_timestamp)
    return (now - last_seen) > timedelta(hours=threshold_hours)
