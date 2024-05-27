import hashlib
import itertools
from string import printable
from multiprocessing import cpu_count, Process, Value

def sha224_hash(text):
    return hashlib.sha224(text.encode()).hexdigest()

dic = printable[:95]

def pass_gen():
    for le in range(1, 5):  
        for c in itertools.product(dic, repeat=le):
            yield ''.join(c)

def cracking(password_hash, found):
    for pas in pass_gen():
        if sha224_hash(pas) == password_hash:
            if found.value == 0:
                print(f'Ваш пароль взломали! Ваш пароль: "{pas}".')
                found.value = 1  
            break

if __name__ == '__main__':
    print('Введите пароль на английском до 4 символов')
    pas = input('Введите пароль: ')

    password_hash = sha224_hash(pas)

    c = cpu_count()
    found= Value('i', 0)
    pr = []
    for _ in range(c):
        p = Process(target=cracking, args=(password_hash, found))
        pr.append(p)
        p.start()
        
    for p in pr:
        p.join()
        if found.value == 1:
            break
