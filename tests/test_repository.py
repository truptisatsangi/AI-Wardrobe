from models import Cloth
from repository.wardrobe_repository import WardrobeRepository


def test_add_cloth():
    repository = WardrobeRepository()

    cloth = Cloth(
        id="1",
        name="T-shirt",
        colour="Black",
        occasion="Casual"
    )

    repository.add_cloth(cloth)

    assert repository.clothes["1"] == cloth


def test_get_cloth():
    repository = WardrobeRepository()

    cloth = Cloth(
        id="1",
        name="T-shirt",
        colour="Black",
        occasion="Casual"
    )

    repository.add_cloth(cloth)

    result = repository.get_cloth("1")

    assert result == cloth


def test_get_cloth_returns_none_when_not_found():
    repository = WardrobeRepository()

    result = repository.get_cloth("999")

    assert result is None


def test_get_all_clothes():
    repository = WardrobeRepository()

    cloth1 = Cloth(
        id="1",
        name="T-shirt",
        colour="Black",
        occasion="Casual"
    )

    cloth2 = Cloth(
        id="2",
        name="Shirt",
        colour="Blue",
        occasion="Office"
    )

    repository.add_cloth(cloth1)
    repository.add_cloth(cloth2)

    result = repository.get_all_clothes()

    assert len(result) == 2
    assert cloth1 in result
    assert cloth2 in result


def test_update_cloth():
    repository = WardrobeRepository()

    cloth = Cloth(
        id="1",
        name="T-shirt",
        colour="Black",
        occasion="Casual"
    )

    repository.add_cloth(cloth)

    updated_cloth = Cloth(
        id="1",
        name="Formal Shirt",
        colour="White",
        occasion="Office"
    )

    repository.update_cloth("1", updated_cloth)

    result = repository.get_cloth("1")

    assert result == updated_cloth
    assert result.name == "Formal Shirt"


def test_delete_cloth():
    repository = WardrobeRepository()

    cloth = Cloth(
        id="1",
        name="T-shirt",
        colour="Black",
        occasion="Casual"
    )

    repository.add_cloth(cloth)

    repository.delete_cloth("1")

    assert repository.get_cloth("1") is None