class Genre:
    def __init__(self,name):
        self.name = name
        self.Origins = 'Техно'
        self.direction = 'Напавление: Электронная танцевальная музыка'
        self.Years_of_Prosperity = 'Рассвет: 1990-е – 2000-е'
    def display_info(self):
        print(f"{self.direction} ")
        print(f"Истоки: {self.Origins} ")
        print(f"{self.Years_of_Prosperity}")
    def nam(self):
        print('Транс')


class Ganre2(Genre):
    def nam(self):
        print('Псайтранс')
    def gde(self):
        print('Популярен в Западной Европе, Скандинавии, Израиле и России')
    def hara(self):
        print('Направление в электронной музыке, отделившееся от гоа-транса в середине 1990-х годов. ')

class Ganre3(Ganre2):
    def nam(self):
        print('Дарк Псайтранс')
    def gde(self):
        print('Популярен в в России и Германии')
    def hara(self):
        print('Наиболее быстрое и искажённое ответвление психоделик-транса, с ускоренным бит-ритмом (145—180 ударов в минуту) ')


trans = Genre('Транс')
trans.nam()
trans.display_info()
print("\n")
Psy = Ganre2('Транс')
Psy.nam()
Psy.hara()
Psy.gde()
Psy.display_info()
print("\n")
DPsy = Ganre3('Транс')
DPsy.nam()
DPsy.hara()
DPsy.gde()
DPsy.display_info()