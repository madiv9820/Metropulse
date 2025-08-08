import sqlite3
from configs.settings import DB_PATH

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Traffic sensor table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS traffic (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            vehicle_count INTEGER,
            avg_speed REAL
        );
    """)

    # Pollution sensor table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pollution (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            pm25 REAL,
            pm10 REAL,
            no2 REAL
        );
    """)

    # Weather sensor table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            temperature REAL,
            humidity REAL,
            wind_speed REAL
        );
    """)

    conn.commit()
    conn.close()
    print("✅ Tables created successfully.")

if __name__ == "__main__":
    create_tables()