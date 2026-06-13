from fastapi import FastAPI, HTTPException
from services import WardrobeService
from repository.wardrobe_repository import WardrobeRepository
from models import ClothCreate, ClothUpdate, Cloth
from exceptions.cloth_exceptions import ClothNotFoundError

app = FastAPI()

wardrobe_repository = WardrobeRepository()
wardrobe_service = WardrobeService(wardrobe_repository)

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Wardrobe"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/clothes")
def add_cloth(cloth: ClothCreate) -> Cloth:
   cloth =  wardrobe_service.add_cloth(Cloth)
   return cloth

@app.get("/clothes/{id}")
def get_cloth(id: str) -> Cloth:
    try:
        return wardrobe_service.get_cloth(id)
    except ClothNotFoundError as e:
        raise HTTPException(status_code=404, details=str(e))

@app.get("/clothes")
def get_all_clothes() -> list[Cloth]:
    return wardrobe_service.get_all_clothes()

@app.patch("/clothes/{id}")
def update_cloth(id: str, update: ClothUpdate) -> Cloth:
    try:
        wardrobe_service.update_cloth_data(id, update)
    except ClothNotFoundError as e:
        raise HTTPException(status_code=404, details=str(e))

@app.delete("/clothes/{id}")
def delete_cloth(id:str) -> bool:
    try:
        response = wardrobe_service.delete_cloth(id)
        return response
    except ClothNotFoundError as e:
        raise HTTPException(status_code=404, details=str(e))

