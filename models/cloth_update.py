from pydantic import BaseModel

class ClothUpdate(BaseModel):
    name: str | None = None
    colour: str | None = None
    occasion: str | None = None

    
