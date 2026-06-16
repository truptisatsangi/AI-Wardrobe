from fastapi import FastAPI
from api.cloth_routes import router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to AI Wardrobe"}

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(router)