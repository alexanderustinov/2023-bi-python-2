import os.path
from string import digits, ascii_letters, punctuation
from passlib.hash import argon2
from multiprocessing import cpu_count, Process, Value

DICTIONARY = [' '] + list(digits + ascii_letters + punctuation)
LENGTH = len(DICTIONARY)
PASSWORD_LEN = 10
CPU_NUM = cpu_count()

h = ''
file_path = '.hash'
if not os.path.exists(file_path):
    print('Ошибка 404: Файл не найден')
    exit()
with open(file_path, 'r') as f:
    h = f.readline().strip()

def word(index):
    password = []
    while index > 0:
        index, remainder = divmod(index, LENGTH)
        if remainder == 0:
            remainder = 1
        password.insert(0, DICTIONARY[remainder])
    return ''.join(password)

def check(c,f):
    for i in range(c, LENGTH ** PASSWORD_LEN, CPU_NUM):
        if i % (CPU_NUM*1000+c):
            if f.value:
                exit()
        password=word(i)
        # print(password)
        if argon2.verify(password, h):
            print(password)
            f.value = 1
            exit()


def main():
    flag = Value('i', 0)
    processes = []
    for i in range(CPU_NUM):
        processes.append(Process(target=check, args=(i,flag)))
        processes[-1].start()
       


if __name__ == '__main__':
    main()