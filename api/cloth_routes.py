from fastapi import HTTPException, APIRouter
from services import WardrobeService
from repository.wardrobe_repository import WardrobeRepository
from models import ClothCreate, ClothUpdate, Cloth
from exceptions.cloth_exceptions import ClothNotFoundError

router = APIRouter(prefix="/clothes", tags=["clothes"])

wardrobe_repository = WardrobeRepository()
wardrobe_service = WardrobeService(wardrobe_repository)

@router.post("/")
def add_cloth(cloth: ClothCreate) -> Cloth:
   cloth =  wardrobe_service.add_cloth(name=cloth.name, colour=cloth.colour, occasion=cloth.occasion)
   return cloth

@router.get("/{id}")
def get_cloth(id: str) -> Cloth:
    try:
        return wardrobe_service.get_cloth(id)
    except ClothNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/")
def get_all_clothes() -> list[Cloth]:
    return wardrobe_service.get_all_clothes()

@router.patch("/{id}")
def update_cloth(id: str, update: ClothUpdate) -> Cloth:
    try:
       return wardrobe_service.update_cloth_data(id, update)
    except ClothNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}")
def delete_cloth(id:str) -> bool:
    try:
        response = wardrobe_service.delete_cloth(id)
        return response
    except ClothNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

