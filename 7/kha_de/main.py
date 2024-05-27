from crack import cracking, dict
from multiprocessing import cpu_count, Process, Value

if __name__ == '__main__':
    l = len(dict)
    c = cpu_count()
    password = open('password.txt').read()
    f = Value('i', 0)
    processes = []
    for i in range(c):
        d = int(l/c) + 1
        p = Process(target = cracking, args = (password, i, d, f))
        processes.append(p)
        processes[-1].start()
    f = True
    while f:
        for p in processes:
            if not (p.is_alive()):
                f = False
                for j in processes:
                    j.terminate()