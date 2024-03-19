from dataclasses import dataclass


@dataclass
class Dog:
    name: str
    age: int


d = Dog("Bob", "3")


from pydantic import BaseModel

from typing import Iterable, Tuple


class Cat(BaseModel):
    name: str
    age: int
    colors: Iterable[str]
    dimensions: Tuple[int|float, int|float]


c = Cat(name="Eve", age=6, colors=["grey", "magenta"], dimensions=(1, 2.5))
print(type(d.age), type(c.age))
