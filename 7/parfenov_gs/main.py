from cracking import dicti, crack_process, hash_creating
from multiprocessing import cpu_count, Process, Value

if __name__ == '__main__':
    lenn = len(dicti)
    cpus = cpu_count()
    password = hash_creating((input('Enter the password, please!\n')))
    flag = Value('i', 0)
    processes = []
    a = 0
    for _ in range(cpus):
        p = Process(target=crack_process, args=(password, a))
        processes.append(p)
        processes[-1].start()
    flag = True
    while flag:
        for p in processes:
            if not (p.is_alive()):
                flag = False
                for __ in processes:
                    __.terminate()