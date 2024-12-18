# Ввод трехзначного числа
number = int(input("Введите трехзначное число: "))

# Извлечение цифр
hundreds = number // 100           # Сотни
tens = (number // 10) % 10         # Десятки
units = number % 10                # Единицы

# Проверка уникальности цифр
all_different = (hundreds != tens) and (hundreds != units) and (tens != units)

# Вывод результата
print("Все цифры данного числа различны:", all_different)
