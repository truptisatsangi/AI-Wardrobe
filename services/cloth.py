from repository.wardrobe_repository import WardrobeRepository
from models.cloth import Cloth
from exceptions.cloth_exceptions import ClothNotFoundError

class WardrobeService:
    def __init__(self,repository: WardrobeRepository):
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
    
    def get_clothes_for_occasion(self, occasion: str) -> Cloth:
        clothes = self.repository.get_all_clothes()
        return [cloth for cloth in clothes if cloth.ocassion.lower() == occasion.lower()]
    
    def update_cloth_data(self, cloth_id: str, cloth_name:str, cloth_colour:str,  cloth_occasion:str) -> Cloth:
        cloth_to_be_updated = self.repository.get_cloth(cloth_id)

        if cloth_to_be_updated:
            updated_cloth = Cloth(id = cloth_id, name=cloth_name, colour=cloth_colour, occasion=cloth_occasion)
            self.repository.update_cloth(cloth_id, updated_cloth)
            return updated_cloth

        raise ClothNotFoundError(f"Cloth {cloth_id} not found")

    def remove_cloth(self, cloth_id: str) -> bool:
        cloth = self.repository.get_cloth(cloth_id)

        if cloth:
            self.repository.remove_cloth(cloth_id)
            return True
        
        raise ClothNotFoundError(f"Cloth {cloth_id} not found")



