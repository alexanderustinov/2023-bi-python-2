import timeit
from hashlib import md5, sha512, blake2b
from passlib.hash import md5_crypt
import time

number = 2000
word = b'hello'

def benchmark(hash_class):
    return hash_class(word).hexdigest()

def benchmark_passlib():
    return md5_crypt.hash(word)


for hash_name, hash_class in zip(('md5', 'sha512', 'blake2b'), (md5, sha512, blake2b)):
    r = timeit.timeit(lambda: benchmark(hash_class), number=number)
    print(f"{hash_name} {r/number}")

r = timeit.timeit(benchmark_passlib, number=number)
print(f"md5_crypt {r/number}")
