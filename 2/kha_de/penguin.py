import webbrowser as wb

class Penguin:
    def __init__(self, species, height, age,  *weight):
        self.species = species
        self.height = height
        self.weight = weight
        self.age = age

    def swim(self):
        print(f"{self.species} хорошо и быстро плавают и ныряют.")
        print(f"Самцы этого вида достигают роста {self.height} см и весят в среднем от {self.weight[0]} до {self.weight[1]} кг.")
        print(f"Естественный возраст этих птиц может достигать {self.age} лет.")

    def find(self):
        species = self.species
        wb.open('https://yandex.ru/search/?text=' + species)

    def baby_bird(self):
        baby = input ('Ввести "яйцо" или "птенец": ')
        wb.open('https://yandex.ru/images/search?from=tabbar&text=' + baby + ' ' + self.species)