from cracking import crack, dict
from multiprocessing import cpu_count, Process, Value

if __name__ == '__main__':
    length = len(dict)
    c = cpu_count()
    password = open('password.txt').read()
    flag = Value('i', 0)
    processes = []
    for i in range(c):
        d = int(length/c) + 1
        p = Process(target=crack, args=(password, i, d, flag))
        processes.append(p)
        processes[-1].start()
    flag = True
    while flag:
        for p in processes:
            if not (p.is_alive()):
                f = False
                for _ in processes:
                    _.terminate()