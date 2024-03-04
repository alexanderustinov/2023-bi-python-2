from math import pi, sqrt
class Stars:
    def __init__(self, radius, mass, distance):
        self.radius = radius
        self.mass = mass
        self.distance = distance

    def density(self):
        density = self.mass / ((4 / 3) * pi * self.radius ** 3)
        return f'{density} кг/м^3'

    def acceleration(self):
        acceleration = (6.67*10**(-11) * self.mass) / (self.radius ** 2)
        return f'{acceleration} м/с^2'

    def removal_speed(self):
        removal_speed = 74.03 * self.distance
        return f'{removal_speed} км/с'


class Planets:
    def __init__(self, radius, rotation_speed, mass, height):
        self.radius = radius
        self.mass = mass
        self.rotation_speed = rotation_speed
        self.height = height

    def rotation_period(self):
        rotation_period = (2*pi*self.radius) / self.rotation_speed
        return f'{rotation_period} с'

    def angular_velocity(self):
        angular_velocity = 2*pi / ((2*pi*self.radius) / self.rotation_speed)
        return f'{angular_velocity} рад/с'

    def first_cosmic_velocity(self):
        first_cosmic_velocity = sqrt((6.6743*10**(-11)*self.mass) / (self.radius + self.height))
        return f'{first_cosmic_velocity} км/с'



class TerrestrialPlanets(Planets):
    def rings(self):
        return f'У планет земной группы отстутсвуют кольца'

    def surface(self):
        return f'У всех планет земной группы твердая поверхность'

    def satellites(self):
        return f'У Земли спутник Луна, у Марса спутники Фобос и Деймос, у Венеры и Меркурия - ни одного'



class GiantPlanets(Planets):
    def rings(self):
        return f'У всех планет-гигантов есть кольца'

    def surface(self):
        return f'Планеты-гиганты не имеют твердой поверхности'

    def satellites(self):
        return f'У Сатурна 15 спутников, у Юпитера - 14, у Урана - 5, у Нептуна - 2'
