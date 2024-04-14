from itertools import product 
from string import ascii_lowercase
from hashlib import sha3_512
from multiprocessing import cpu_count, Pool


hash_was = 'ec2733518340c350aba3cb7171f952590b71d6c76b2701f88868d238a73f6a8e349e51231be0685ef39f511d40facda09b8009add05f7a079b89d32961297611'


def enumeration_func(gen):
    word_now = ''.join(gen)
    hash_now = sha3_512(word_now.encode()).hexdigest()
    if hash_now == hash_was:
        print(f"password seems to be '{word_now}'")
        return word_now
    return False


if __name__ == '__main__':

    for i in range(8):
        print('word length:', i + 1)
        gen = product(ascii_lowercase, repeat=i+1)
        lst = []
        for i in gen:
            lst.append(i)
        with Pool(cpu_count()) as p:
            res = p.map(enumeration_func, lst)
            if any(res):
                p.terminate()
                break
    else:
        print('password not found')
