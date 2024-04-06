from itertools import product
import hashlib
from string import printable


def hashing(word: str): # Решил всё хэшить в функции
    return hashlib.blake2s(word.encode()).hexdigest()


m_dict = printable[:95] # Решил сразу всё кроме таба, ньюлайна и прочей непаролльной нечести.


def get_first_l(num_p, delta): # первая буква для конкретного процесса. Чтоб параллелить.
    return m_dict[num_p*delta:(num_p+1)*delta]


def genering(leng: int, num_p: int, delta: int): # список слов нужной длины для конкретного процесса
    g_lizt = []
    alizt = product(m_dict, repeat=leng-1)
    lizt = [''.join(y) for y in alizt]
    for l in get_first_l(num_p, delta):
        n_lizt = [l+s for s in lizt]
        for h in n_lizt:
            g_lizt.append(h) # страшно,но работает, хотя ничего трудного
    return g_lizt


def comparing(hasz, num_p, delta, f): # сама функция
    lengo = 1
    while True:
        if f.value == 1:
            break
        for word in genering(lengo, num_p, delta):
            if hasz == hashing(word):
                print('Взлом завершен. Пароль: ', word)
                f.value = 1
                break
        lengo += 1

