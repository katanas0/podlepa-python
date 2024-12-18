# Ввод двух чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

# Определение меньшего числа
if a < b:
    smaller_index = 1
else:
    smaller_index = 2

# Вывод результата
print("Порядковый номер меньшего числа:", smaller_index)