
X = float(input("Введите вещественное число X (|X| < 1): "))
N = int(input("Введите целое число N (>0): "))
if abs(X) >= 1 or N <= 0:
    print("Некорректные входные данные!")
else:
    result = sum(((-1) ** (i - 1)) * (X ** i) / i for i in range(1, N + 1))
    print("Приближенное значение ln(1 + X):", result)