CREATE TABLE sensor_health_logs (
    id SERIAL PRIMARY KEY,
    sensor_id TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('active', 'inactive')),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
