from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psutil
import time

app = FastAPI(
    title="VisionEdge API",
    description="AI-powered Edge Video Analytics Backend",
    version="1.0.0"
)

# Allow the dashboard/frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

start_time = time.time()


@app.get("/")
def home():
    return {
        "project": "VisionEdge",
        "status": "running",
        "message": "VisionEdge backend is working"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "VisionEdge Backend"
    }


@app.get("/telemetry")
def telemetry():
    memory = psutil.virtual_memory()

    return {
        "cpu_usage": psutil.cpu_percent(interval=0.2),
        "memory_usage": memory.percent,
        "memory_available_gb": round(memory.available / (1024 ** 3), 2),
        "uptime_seconds": round(time.time() - start_time, 2),
        "stream_status": "ready"
    }


@app.get("/cameras")
def cameras():
    return {
        "cameras": [
            {
                "id": "CAM-01",
                "name": "Demo Camera",
                "status": "ready"
            }
        ]
    }
