from hashlib import sha384
from string import printable

def hash(password):
    return sha384(password.encode()).hexdigest()

dict = printable[:95]

def first_letter(n, d):
    return dict[n * d:(n + 1) * d]

def next_word(lst: list):
    length = len(lst)
    if length == 1 and lst[0] == 94:
        return None
    if lst[0] != 94:
        lst[0] += 1
        return lst
    else:
        i = 1
        while lst[i] == 94 and i <= length - 2:
            i += 1
        if i == length - 1 and lst[i] == 94:
            return None
        lst[i] += 1
        for j in range(i):
            lst[j] = 0
        return lst

def crack(hash_input, n, d, flag):
    length = 1
    for password_word in first_letter(n, d):
        if hash_input == hash(password_word):
            print(f'I know your password, and it is: "{password_word}"')
            flag.value = 1
            break

    while not flag.value:
        word_list = [0] * length
        length += 1
        r = 0
        while word_list is not None:
            password_word = ''.join(dict[i] for i in word_list)
            for i in first_letter(n, d):
                if hash(i + password_word) == hash_input:
                    print(f'I know your password, and it is: "{i + password_word}".')
                    flag.value = 1
                    break
            word_list = next_word(word_list)
            r += 1
            if r % 100000 == 0:
                if flag.value == 1:
                    break