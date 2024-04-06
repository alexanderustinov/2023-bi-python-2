from funcs import hashing

# Решил всё везде закидать комментариями. Тут нечего писать...

pasw = input('Добрый день! Введите свой пароль для взлома: ')

with open('m_pass.txt', 'w') as file:
    file.write(hashing(pasw))
