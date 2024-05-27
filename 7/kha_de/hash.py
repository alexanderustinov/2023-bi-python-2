from crack import hashing

password = input('Hello! Enter the password: ')

with open('password.txt', 'w') as file:
    file.write(hashing(password))