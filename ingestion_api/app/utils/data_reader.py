import sqlite3
import json
from pathlib import Path
from app.configs.settings import DB_PATH, LOCAL_PATH

def read_from_db(sensor_type: str):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {sensor_type} ORDER BY id DESC LIMIT 5')

    rows = cur.fetchall()
    return [dict(row) for row in rows]

def read_from_file(sensor_type: str):
    folder_path = Path(LOCAL_PATH) / sensor_type
    data_files = folder_path.glob('*.json')
    all_data = []

    for file in data_files:
        with open(file, 'r') as f:
            data = json.load(f)
            all_data.append(data)

    return all_data