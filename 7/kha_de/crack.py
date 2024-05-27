from hashlib import sha256
from string import printable

def hashing(password):
    return sha256(password.encode()).hexdigest()

dict = printable[:95]

def first_letter(n, d):
    return dict[n * d:(n + 1) * d]

def next_word(lst: list):
    l = len(lst)
    if l == 1 and lst[0] == 94:
        return None
    if lst[0] != 94:
        lst[0] += 1
        return lst
    else:
        j = 1
        while lst[j] == 94 and j <= l - 2:
            j += 1
        if j == l - 1 and lst[j] == 94:
            return None
        lst[j] += 1
        for a in range(j):
            lst[a] = 0
        return lst

def cracking(hash_is, n, d, f):
    l = 1
    for word in first_letter(n, d):
        if hash_is == hashing(word):
            print(f'We cracked it! Password is "{word}".')
            f.value = 1
            break

    while not f.value:
        word_list = [0] * l
        l += 1
        r = 0
        while word_list is not None:
            word = ''.join(dict[i] for i in word_list)
            for j in first_letter(n, d):
                if hashing(j + word) == hash_is:
                    print(f'We cracked it! Password is "{j + word}".')
                    f.value = 1
                    break
            word_list = next_word(word_list)
            r += 1
            if r % 100000 == 0:
                if f.value == 1:
                    break