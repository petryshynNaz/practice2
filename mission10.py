# Завдання 10
k = int(input("Введіть число k: "))

a = int(input("Введіть ціле число a: "))
b = int(input("Введіть ціле число b: "))
c = int(input("Введіть ціле число c: "))

divisors = []

if a % k == 0:
    divisors.append(a)
if b % k == 0:
    divisors.append(b)
if c % k == 0:
    divisors.append(c)

if divisors:
    print("Число k є дільником наступних чисел:", divisors)
else:
    print("Число k не є дільником жодного з чисел a, b, c.")
