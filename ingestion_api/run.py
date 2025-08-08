from fastapi import FastAPI
from app.routes import ingest_routes, fetch_routes

app = FastAPI(title = "Metropulse Smarcity Ingestion API")
app.include_router(ingest_routes.router)
app.include_router(ingest_routes.router, prefix = '/ingest', tags = ['Ingestion'])
app.include_router(fetch_routes.router, prefix = '/fetch', tags = ['Extraction'])

@app.get("/health")
def health_check():
    return {"status": "Metropulse API is UP"}

'''
curl -X POST "http://localhost:8000/ingest/local/traffic" -H "Content-Type: application/json" -d '{"sensor_id":"T123","timestamp":"2025-08-08T10:30:00","vehicle_count":120,"avg_speed":45.5}'
curl -X POST "http://localhost:8000/ingest/db/traffic" -H "Content-Type: application/json" -d '{"sensor_id":"T123","timestamp":"2025-08-08T10:30:00","vehicle_count":120,"avg_speed":45.5}'

curl -X POST "http://localhost:8000/ingest/local/pollution" -H "Content-Type: application/json" -d '{"sensor_id":"P456","timestamp":"2025-08-08T12:00:00","pm25":35.2,"pm10":55.4,"no2":24.8}'
curl -X POST "http://localhost:8000/ingest/db/pollution" -H "Content-Type: application/json" -d '{"sensor_id":"P456","timestamp":"2025-08-08T12:00:00","pm25":35.2,"pm10":55.4,"no2":24.8}'

curl -X POST "http://localhost:8000/ingest/local/weather" -H "Content-Type: application/json" -d '{"sensor_id":"W789","timestamp":"2025-08-08T12:30:00","temperature":30.5,"humidity":60.2,"wind_speed":12.4}'
curl -X POST "http://localhost:8000/ingest/db/weather" -H "Content-Type: application/json" -d '{"sensor_id":"W789","timestamp":"2025-08-08T12:30:00","temperature":30.5,"humidity":60.2,"wind_speed":12.4}'
'''