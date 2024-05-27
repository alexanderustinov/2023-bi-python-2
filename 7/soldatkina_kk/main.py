from crack import cracking, diction
from multiprocessing import cpu_count, Process, Value

if __name__ == '__main__':
    ls = len(diction)
    c = cpu_count()
    password = open('pass.txt').read()
    Flag = Value('i', 0)
    processes = []
    for i in range(c):
        k = int(ls/c) + 1
        p = Process(target = cracking, args = (password, i, k, Flag))
        processes.append(p)
        processes[-1].start()
    Flag = True
    while Flag:
        for p in processes:
            if not (p.is_alive()):
                Flag = False
                for j in processes:
                    j.terminate()