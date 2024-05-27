from pydantic import BaseModel
from typing import Iterable
import webbrowser as wb

class Penguin(BaseModel):
    species: str
    height: int
    weight: Iterable[int]
    age: int

    def swim(self):
        print(f"{self.species} хорошо и быстро плавают и ныряют.")
        print(f"Самцы этого вида достигают роста {self.height} см и весят в среднем от {self.weight[0]} до {self.weight[1]} кг.")
        print(f"Естественный возраст этих птиц может достигать {self.age} лет.")

    def find(self):
        species = self.species
        wb.open('https://yandex.ru/search/?text=' + species)