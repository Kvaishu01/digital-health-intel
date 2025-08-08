from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Digital Health Intel API")

# Allow frontend (Streamlit) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Digital Health Intel API is running!"}

@app.post("/predict")
async def predict(data: dict):
    # For now, just return the input — later we connect ML models here
    return {"received_data": data}
