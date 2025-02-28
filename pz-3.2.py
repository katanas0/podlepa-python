
number = int(input("Введите трехзначное число: "))
hundreds = number // 100           # Сотни
tens = (number // 10) % 10         # Десятки
units = number % 10                # Единицы
all_different = (hundreds != tens) and (hundreds != units) and (tens != units)
print("Все цифры данного числа различны:", all_different)
