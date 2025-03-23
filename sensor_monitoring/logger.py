import psycopg2

def log_offline_sensors(sensor_ids, conn_params):
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()
    for sensor_id in sensor_ids:
        cursor.execute("INSERT INTO sensor_health_logs (sensor_id, status) VALUES (%s, 'inactive')", (sensor_id,))
    conn.commit()
    cursor.close()
    conn.close()
