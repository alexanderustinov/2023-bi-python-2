import webbrowser
from random import choice

all_language = ['Ассемблер','Фортан','Бейсик','Паскаль','Си','Си++','Visual','Basic','Delphi','Java','Python','Пролог','Лисп']
right_proc = ['Ассемблер','Фортан','Бейсик','Паскаль','Си']
right_nproc = ['Си++','Visual','Basic','Delphi','Java','Python','Пролог','Лисп']
s = choice(all_language)
print(s)
class Lang:
    def __init__(self):
        print('Ваш язык программирования:')

    def npr(self):
        if s in right_proc:
            print('Процедурный')
        elif s in right_nproc:
            print('Непроцедурный')

    def osh(self):
        if s not in right_nproc and s not in right_proc:
            print('Вы неверно ввели название языка программирования')
            exit()
class Proc(Lang):
    def __init__(self):
        print(end='\r')

    def h_l(self):
        if s == 'Ассемблер':
            print('Низкого уровня//машинно-зависимый')
        elif s != 'Ассемблер' and s in right_proc:
            print('Выского уровня//машинно-независимый')

    def new_inf(self):
        print('Больше информации о классификации языков программирования:')
        webbrowser.open(
            'https://spravochnick.ru/programmirovanie/yazyki_programmirovaniya/klassifikaciya_yazykov_programmirovaniya/')
class Nproc(Lang):
    def __init__(self):
        print(end='\r')

    def dec(self):
        if s == 'Пролог' or s == 'Лисп':
            print('Декларативный')
        elif s != 'Пролог' and s != 'Лисп' and s in right_nproc:
            print('Объектно-ориентированный')

    def new_inf(self):
        print('Больше информации о классификации языков программирования:')
        webbrowser.open(
            'https://spravochnick.ru/programmirovanie/yazyki_programmirovaniya/klassifikaciya_yazykov_programmirovaniya/')
l = Lang()
l.npr()
c = Proc()
c.osh()
c.h_l()
f = Nproc()
f.dec()
f.new_inf()
