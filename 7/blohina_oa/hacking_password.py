from multiprocessing import Process
from itertools import product
from string import ascii_letters
from hashlib import md5
from my_pass import pasw_hash

hash_was = pasw_hash

def find_password():
    for i in range(6):
        gen = product(ascii_letters, repeat = i+1)
        found = False
        while True:
            try:
                word_now = ''.join(next(gen))
                hash_now = md5(word_now.encode()).hexdigest()
                if hash_now==hash_was:
                    found = True
                    print(f"password seems to be '{word_now}'")
                    break
            except StopIteration:
                    break
        if found:
            break

if __name__ == "__main__":
    p = Process(find_password())
    p.start()
    p.join()
