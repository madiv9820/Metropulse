import os

BASE_DIR = os.path.dirname(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
DB_PATH = os.path.join(BASE_DIR, 'data', 'db', 'metropulse.db')
LOCAL_PATH = os.path.join(BASE_DIR, 'data', 'local')