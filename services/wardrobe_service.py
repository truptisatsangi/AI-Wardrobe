from repository.wardrobe_repository import WardrobeRepository
from models import Cloth, ClothUpdate
from exceptions.cloth_exceptions import ClothNotFoundError


class WardrobeService:
    def __init__(self, repository: WardrobeRepository):
        self.repository = repository 

    def add_cloth(self, name: str, colour: str, occasion: str) -> Cloth:

        cloth = Cloth(
            name=name, 
            colour=colour, 
            occasion=occasion
        )
        
        self.repository.add_cloth(cloth)
        return cloth

    def get_cloth(self, cloth_id: str) -> Cloth:
        cloth = self.repository.get_cloth(cloth_id)

        if cloth is None:
            raise ClothNotFoundError(f"Cloth {cloth_id} not found")
        
        return cloth
    
    def get_all_clothes(self) -> list[Cloth]:
        return self.repository.get_all_clothes()
    
    def get_clothes_for_occasion(self, occasion: str) -> Cloth:
        clothes = self.repository.get_all_clothes()
        return [cloth for cloth in clothes if cloth.ocassion.lower() == occasion.lower()]
    
    def update_cloth_data(self, cloth_id: str, update: ClothUpdate) -> Cloth:
        cloth = self.repository.get_cloth(cloth_id)

        if cloth is None:
            raise ClothNotFoundError(f"Cloth {cloth_id} not found")
        
        if update.name is not None:
            cloth.name = update.name
        
        if update.colour is not None:
            cloth.colour = update.colour
            
        if update.occasion is not None:
            cloth.occasion = update.occasion

        self.repository.update_cloth(cloth_id, cloth)
        return cloth
            

    def delete_cloth(self, cloth_id: str) -> bool:
        cloth = self.repository.get_cloth(cloth_id)

        if cloth:
            self.repository.delete_cloth(cloth_id)
            return True
        
        raise ClothNotFoundError(f"Cloth {cloth_id} not found")



