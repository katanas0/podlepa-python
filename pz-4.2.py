N = int(input("Введите целое число N (>0): "))
is_power_of_3 = False
if N > 0:
    while N % 3 == 0:
        N //= 3
    is_power_of_3 = (N == 1)
print("Является ли число степенью 3:", is_power_of_3)