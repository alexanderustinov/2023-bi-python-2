import hashlib
from string import printable


def hashing(word):  # Решил всё хэшить в функции
    return hashlib.blake2s(word.encode()).hexdigest()


m_dict = printable[:95]  # Решил сразу всё кроме таба, ньюлайна и прочей непаролльной нечести.


def get_first_l(num_p, delta):  # первая буква для конкретного процесса. Чтоб параллелить.
    return m_dict[num_p*delta:(num_p+1)*delta]


def next_list(l_ist: list):  # следующее слово

    l = len(l_ist)

    if l == 1 and l_ist[0] == 94:
        return None

    if l_ist[0] != 94:
        l_ist[0] += 1
        return l_ist
    else:  # первый точно 94
        j = 1
        while l_ist[j] == 94 and j <= l - 2: # первый элемент не равный 94
            j += 1
        if j == l - 1 and l_ist[j] == 94: # последний уже 94
            return None
        l_ist[j] += 1  # увеличился разряд
        for a in range(j):
            l_ist[a] = 0  # все меньшие его обнулились
        return l_ist


def comparing(hasz, num_p, delta, f):  # сама функция
    lengo = 1  # начало

    for word in get_first_l(num_p, delta):  # тривиальный
        if hasz == hashing(word):
            print('Взлом завершен. Пароль: ', word)
            f.value = 1
            break

    while not f.value:
        word_list = [0] * lengo  # слово начало
        lengo += 1
        r=0
        while word_list is not None:  # пока все не прошли
            word = ''.join(m_dict[i] for i in word_list)  # сделал слово
            for fl in get_first_l(num_p, delta):  # подставил все первые буквы процесса
                if hashing(fl + word) == hasz:
                    print('Взлом завершен. Пароль: ', fl + word)
                    f.value = 1
                    break
            word_list = next_list(word_list)  # следующее слово
            r += 1
            if r%100000==0:  # ну и распараллеленность не пропадает
                if f.value == 1: # и все вместе умирают
                    break
