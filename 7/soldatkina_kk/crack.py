from hashlib import blake2b
from string import printable

def hashing(password):
    return blake2b(password.encode()).hexdigest()

diction = printable[:95]

def first(num, k):
    return diction[num * k:(num + 1) * k]

def next(l: list):
    ls = len(l)
    if ls == 1 and l[0] == 94:
        return None
    if l[0] != 94:
        l[0] += 1
        return l
    else:
        j = 1
        while l[j] == 94 and j <= ls - 2:
            j += 1
        if j == ls - 1 and l[j] == 94:
            return None
        l[j] += 1
        for a in range(j):
            l[a] = 0
        return l

def cracking(hash_is, num, k, f):
    ls = 1
    for word in first(num, k):
        if hash_is == hashing(word):
            print(f'Взлом прошел успешно! Ваш пароль: "{word}".')
            f.value = 1
            break

    while not f.value:
        word_list = [0] * ls
        ls += 1
        r = 0
        while word_list is not None:
            word = ''.join(diction[i] for i in word_list)
            for j in first(num, k):
                if hashing(j + word) == hash_is:
                    print(f'Взлом прошел успешно! Ваш пароль: "{j + word}".')
                    f.value = 1
                    break
            word_list = next(word_list)
            r += 1
            if r % 100000 == 0:
                if f.value == 1:
                    break
