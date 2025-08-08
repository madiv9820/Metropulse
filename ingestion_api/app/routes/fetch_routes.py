from fastapi import APIRouter, HTTPException
from app.utils.data_reader import read_from_db, read_from_file

router = APIRouter()

@router.get('/{source_type}/{sensor_type}')
def fetch_data(source_type: str, sensor_type: str):
    source_map = {'db': read_from_db, 'local': read_from_file}
    model_map = {'traffic', 'pollution', 'weather'}

    if sensor_type not in model_map:
        raise HTTPException(status_code = 400, detail = 'Invalid sensor_type')
    if source_type not in source_map:
        raise HTTPException(status_code = 400, detail = 'Invalid source_type')
    
    return source_map[source_type](sensor_type)