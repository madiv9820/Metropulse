from fastapi import APIRouter, HTTPException, Body
from app.models import TrafficSensorData, PollutionSensorData, WeatherSensorData
from app.utils.file_writer import save_to_local, save_to_db

router = APIRouter()

@router.get("/api/v1/hello")
def hello():
    return {"message": "Welcome to Metropulse Ingestion API"}

@router.post('/{store_type}/{sensor_type}')
def ingest_data(store_type: str, sensor_type: str, payload: dict = Body(...)):
    store_map = {'local': save_to_local, 'db': save_to_db}
    model_map = {
        'traffic': TrafficSensorData,
        'pollution': PollutionSensorData,
        'weather': WeatherSensorData
    }

    if store_type not in store_map:
        raise HTTPException(status_code = 400, detail = 'Invalid store_type')

    if sensor_type not in model_map:
        raise HTTPException(status_code = 400, detail = 'Invalid sensor_type')
    
    try:
        validated_data = model_map[sensor_type](**payload)
    except Exception as e:
        raise HTTPException(status_code = 422, detail = f'Validation Error: {str(e)}')

    store_map[store_type](sensor_type, validated_data.dict())
    return {'status': 'success', 'message': f'{sensor_type} data ingested'}