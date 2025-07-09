from fastapi import APIRouter

router = APIRouter()

@router.get("/api/v1/hello")
def hello():
    return {"message": "Welcome to Metropulse Ingestion API"}