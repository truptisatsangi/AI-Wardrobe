from models import ClothCreate, ClothUpdate, Cloth
from repository.wardrobe_repository import WardrobeRepository


def test_add_cloth():

    warddrobe_repository = WardrobeRepository()
    test_cloth = Cloth(id="1", name="T-shirt", colour="Black", occasion="Casual")
    warddrobe_repository.add_cloth(test_cloth)
    assert warddrobe_repository.clothes["1"] == test_cloth

def test_get_cloth():
    pass

def test_get_cloth_returns_none_when_not_found():
    pass

def test_get_all_clothes():
    pass

def test_update_cloth():
    pass

def test_delete_cloth():
    pass