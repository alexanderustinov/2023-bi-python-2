class Tee ():
    #описание чая
    def __init__(self, type_of_fermentation, portions):
        self.type_of_fermentation = type_of_fermentation
        self.portions = portions
    #человек пьёт чашку чая
    def tea_party (self):
        self.portions -= 1
        print("После чайной паузы в запасе осталось" , self.portions , "порций чая с этикеткой" , self.type_of_fermentation)