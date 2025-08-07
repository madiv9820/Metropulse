from fastapi import APIRouter, HTTPException, Body
from app.models import TrafficSensorData, PollutionSensorData, WeatherSensorData
from app.utils.file_writer import save_to_raw_storage

router = APIRouter()

@router.get("/api/v1/hello")
def hello():
    return {"message": "Welcome to Metropulse Ingestion API"}

@router.post('/{sensor_type}')
def ingest_data(sensor_type: str, payload: dict = Body(...)):
    model_map = {
        'traffic': TrafficSensorData,
        'pollution': PollutionSensorData,
        'weather': WeatherSensorData
    }

    if sensor_type not in model_map:
        raise HTTPException(status_code = 400, detail = 'Invalid sensor_type')
    
    try:
        validated_data = model_map[sensor_type](**payload)
    except Exception as e:
        raise HTTPException(status_code = 422, detail = f'Validation Error: {str(e)}')
    
    save_to_raw_storage(sensor_type, validated_data.dict())
    return {'status': 'success', 'message': f'{sensor_type} data ingested'}