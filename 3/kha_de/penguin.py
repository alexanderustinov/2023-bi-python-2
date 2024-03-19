from random import randint

class Penguin:
    def __init__(self, species, height, age,  *weight):
        self.species = species
        self.height = height
        self.weight = weight
        self.age = age

    def swim(self):
        return (f"Penguin's species - {self.species}. "
                f"Their average height is {self.height} and weight is from {self.weight[0]} to {self.weight[1]} kg. "
                f"Besides, they can reach the age of {self.age}.")

