import sys
from itertools import product 
from string import ascii_lowercase
from hashlib import sha3_512
from multiprocessing import cpu_count, Pool


hash_was = '75d527c368f2efe848ecf6b073a36767800805e9eef2b1857d5f984f036eb6df891d75f72d9b154518c1cd58835286d1da9a38deba3de98b5a53e5ed78a84976'


def enumeration_func(lst):
    for i in lst:
        word_now = ''.join(i)
        hash_now = sha3_512(word_now.encode()).hexdigest()
        if hash_now == hash_was:
            return word_now
    return False


class Worker():
    def __init__(self):
        self.cpu = cpu_count() - 1
        self.pool = Pool(self.cpu)

    def data(self, step):
        gen = product(ascii_lowercase, repeat=step + 1)
        matrix, lst = [], []
        length = 26 ** (3 + 1)
        board = length // self.cpu
        c, k = 1, 1
        for i in gen:
            lst.append(i)
            if c == board * k:
                matrix.append(lst)
                lst = []
                k += 1
            c += 1
        if lst:
            matrix.append(lst)
        return matrix

    def main(self):
        for i in range(8):
            print('word length:', i + 1)
            test = self.pool.map(enumeration_func, self.data(i))
            if any(test):
                print([res for res in test if res][0])
                sys.exit()
        else:
            print('password not found')
        self.pool.close()
        self.pool.join()


if __name__ == '__main__':
    w = Worker()
    w.main()
