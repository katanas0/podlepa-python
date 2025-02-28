number = int(input("Введите трехзначное число: "))
hundreds = number // 100
tens = (number // 10) % 10
units = number % 10
new_number = hundreds * 100 + units * 10 + tens
print("Число после перестановки десятков и единиц:", new_number)