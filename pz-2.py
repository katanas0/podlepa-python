number = int(input("Введите трехзначное число: "))

# Извлечение цифр числа
hundreds = number // 100  # Сотни
tens = (number // 10) % 10  # Десятки
units = number % 10  # Единицы

# Формирование нового числа
new_number = hundreds * 100 + units * 10 + tens

# Вывод результата
print("Число после перестановки десятков и единиц:", new_number)