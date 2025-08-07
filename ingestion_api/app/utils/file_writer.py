import os
import json
from datetime import datetime

def save_to_raw_storage(sensor_type: str, data: dict):
    base_dir = f'data/raw/{sensor_type}'
    os.makedirs(base_dir, exist_ok = True)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S%f")
    file_path = os.path.join(base_dir, f'{timestamp}.json')

    with open(file_path, 'w') as f:
        json.dump(data, f, indent = 4, default = str)