from fastapi import FastAPI
from app.routes import ingest_routes

app = FastAPI(title = "Metropulse Smarcity Ingestion API")
app.include_router(ingest_routes.router)

@app.get("/health")
def health_check():
    return {"status": "Metropulse API is UP"}