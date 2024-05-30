from pydantic import BaseModel


class StarsTest(BaseModel):
    name: str
    radius: float
    mass: float
    distance: float
