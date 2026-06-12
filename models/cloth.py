from pydantic import BaseModel, Field
from uuid import uuid4

class Cloth(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    colour: str
    occasion: str


