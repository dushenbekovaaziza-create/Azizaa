base_num = int(input("Укажите число от 1 до 10: "))

for mult in range(1, 11):
    result = base_num * mult
    print(f"{base_num} x {mult} = {result}")