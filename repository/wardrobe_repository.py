from models.cloth import Cloth

class WardrobeRepository:
    def __init__(self):
        self.clothes : dict[str, Cloth] = {}

    def add_cloth(self, cloth: Cloth):
        self.clothes[cloth.id] = cloth

    def get_cloth(self, cloth_id: str) -> Cloth | None:
        return self.clothes.get(cloth_id)
    
    def get_all_clothes(self) -> list[Cloth]:
        return list(self.clothes.values)
    
    def update_cloth(self, cloth_id: str, cloth: Cloth):
        self.clothes[cloth_id] = cloth

    def remove_cloth(self, cloth_id: str):
        self.clothes.pop(cloth_id, None)





   