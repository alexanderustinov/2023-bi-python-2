import multiprocessing
from multiprocessing import Manager, Process
import hashlib
from string import ascii_letters, digits, punctuation

def get_password_hash():
    password = input("Введите пароль для поиска (не более 4 символов): ")
    hash_object = hashlib.shake_256(password.encode())
    target_hash = hash_object.hexdigest(32)
    print(f"Целевой хеш: {target_hash}")
    return target_hash

def generate_password_from_index(index, symbols, max_length):
    for length in range(1, max_length + 1):
        total_combinations = len(symbols) ** length
        if index < total_combinations:
            password = []
            for _ in range(length):
                index, rem = divmod(index, len(symbols))
                password.append(symbols[rem])
            return ''.join(password)
        index -= total_combinations
    return ""

def divide_search_space(total_symbols, max_length, num_partitions):
    total_combinations = sum(total_symbols ** i for i in range(1, max_length + 1))
    partition_size = total_combinations // num_partitions
    partitions = [(i * partition_size, (i + 1) * partition_size) for i in range(num_partitions)]
    partitions[-1] = (partitions[-1][0], total_combinations)
    print(f"Разделение пространства поиска на {num_partitions} частей.")
    return partitions

def generate_and_check_passwords(partition, target_hash, stop_event, found_password, symbols, max_length):
    start, end = partition
    print(f"Начало обработки диапазона: {start} - {end}")
    for index in range(start, end):
        if stop_event.is_set():
            break
        password = generate_password_from_index(index, symbols, max_length)
        hash_object = hashlib.shake_256(password.encode())
        password_hash = hash_object.hexdigest(32)
        if password_hash == target_hash:
            stop_event.set()
            found_password.value = password
            print(f"Пароль найден: {password}")
            break

def multiprocessing_password_search(target_hash):
    manager = Manager()
    stop_event = manager.Event()
    found_password = manager.Value('d', '')
    symbols = ascii_letters + digits + punctuation
    max_length = 4
    num_partitions = multiprocessing.cpu_count()
    partitions = divide_search_space(len(symbols), max_length, num_partitions)

    processes = [
        Process(target=generate_and_check_passwords, args=(partition, target_hash, stop_event, found_password, symbols, max_length))
        for partition in partitions
    ]

    for process in processes:
        process.start()
    for process in processes:
        process.join()

    if found_password.value:
        print(f"Найденный пароль: {found_password.value}")
    else:
        print("Пароль не найден.")

if __name__ == "__main__":
    target_hash = get_password_hash()
    multiprocessing_password_search(target_hash)
