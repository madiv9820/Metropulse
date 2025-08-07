from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TrafficSensorData(BaseModel):
    sensor_id: str
    timestamp: datetime
    vehicle_count: int
    avg_speed: float

class PollutionSensorData(BaseModel):
    sensor_id: str
    timestamp: datetime
    pm25: float
    pm10: float
    no2: float

class WeatherSensorData(BaseModel):
    sensor_id: str
    timestamp: datetime
    temperature: float
    humidity: float
    wind_speed: float