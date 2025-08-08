import os
import json
import sqlite3
from datetime import datetime
from app.configs.settings import DB_PATH, LOCAL_PATH

def save_to_local(sensor_type: str, data: dict):
    base_dir = os.path.join(LOCAL_PATH, sensor_type)
    print(base_dir)
    os.makedirs(base_dir, exist_ok = True)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S%f")
    file_path = os.path.join(base_dir, f'{timestamp}.json')

    with open(file_path, 'w') as f:
        json.dump(data, f, indent = 4, default = str)

def save_to_db(sensor_type: str, data: dict):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    if sensor_type == 'traffic':
        cur.execute("""
            INSERT INTO traffic (sensor_id, timestamp, vehicle_count, avg_speed)
            VALUES (?, ?, ?, ?)
        """, (
            data['sensor_id'],
            data['timestamp'],
            data['vehicle_count'],
            data['avg_speed']
        ))

    elif sensor_type == 'pollution':
        cur.execute("""
            INSERT INTO pollution (sensor_id, timestamp, pm25, pm10, no2)
            VALUES (?, ?, ?, ?, ?)
        """, (
            data['sensor_id'],
            data['timestamp'],
            data['pm25'],
            data['pm10'],
            data['no2']
        ))

    elif sensor_type == 'weather':
        cur.execute("""
            INSERT INTO weather (sensor_id, timestamp, temperature, humidity, wind_speed)
            VALUES (?, ?, ?, ?, ?)
        """, (
            data['sensor_id'],
            data['timestamp'],
            data['temperature'],
            data['humidity'],
            data['wind_speed']
        ))

    conn.commit()
    conn.close()