from pydantic import BaseModel

from typing import Iterable, Tuple, List


class Cat(BaseModel):
    name: str
    age: int
    colors: List[str]
    dimensions: Tuple[float, float]


