from funcs import comparing, m_dict
from multiprocessing import cpu_count, Process, Value


if __name__ == '__main__':
    le = len(m_dict)
    c = cpu_count()
    passw = open('m_pass.txt').read()
    flag = Value('i', 0)
    processes = []
    for i in range(c):
        delta = int(le/c) + 1 # добавил 1, т.к. может округлиться сильно вниз
        p = Process(target=comparing, args=(passw, i, delta, flag)) # Главное. Главное не Монте-Карло
        processes.append(p)
        processes[-1].start()

    f = True # (The Most Hard Part) Долго с этим мучался.
    while f: # Смог убить их все сразу только так. Иначе они еще живут, или сыпались ошибки.
        for p in processes:
            if not(p.is_alive()): # Только один нашёл. Тут же убил все.
                for pr in processes:
                    pr.terminate()
                f = False







