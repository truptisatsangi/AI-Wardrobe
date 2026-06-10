from pydantic import BaseModel

class Cloth(BaseModel):
    id: str
    name: str
    colour: str
    occassion: str


