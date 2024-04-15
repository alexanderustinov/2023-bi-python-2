from math import pi
from pydantic import BaseModel

class Stars(BaseModel):
    name: str
    radius: float
    mass: float
    distance: float
    def density(self):
        density = self.mass / ((4 / 3) * pi * self.radius ** 3)
        return f'{density} кг/м^3'

    def acceleration(self):
        acceleration = (6.67 * 10 ** (-11) * self.mass) / (self.radius ** 2)
        return f'{acceleration} м/с^2'

    def removal_speed(self):
        removal_speed = 74.03 * self.distance
        return f'{removal_speed} км/с'

