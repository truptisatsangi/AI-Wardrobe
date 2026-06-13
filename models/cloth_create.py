from pydantic import BaseModel

class ClothCreate(BaseModel):
    name: str
    colour: str
    occasion: str