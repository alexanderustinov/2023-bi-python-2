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

r = randint(0, 20)
if r % 2 == 0:
    bird = Penguin('Emperor Penguin', '130', '25', '35', '40')
else:
    bird = Penguin('Rockhopper Penguin', '60', '25', '2', '3')