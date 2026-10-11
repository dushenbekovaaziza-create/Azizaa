import random

target = random.randint(1, 100)
user_num = 0
count_tries = 0

while user_num != target:
    user_num = int(input("Введите число: "))
    count_tries += 1
    
    if user_num < target:
        print("Загаданное число больше!")
    elif user_num > target:
        print("Загаданное число меньше!")

print("Поздравляю! Угадано за", count_tries, "попыток.")