from itertools import product
from string import printable
from hashlib import sha512

dicti = printable[:95]


def hash_creating(word):
    return sha512(word.encode()).hexdigest()


def crack_process(needed_hash, a):
    for j in range(1, 5):
        flag = False
        for i in (product(dicti, repeat=j)):
            hash_now = hash_creating(''.join(i))
            if hash_now == needed_hash:
                print(f"Found it! Your password's hash:{hash_now} and the password itself is: {''.join(i)}")
                flag = True
                break
        if flag:
            break
