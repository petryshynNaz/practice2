# Завдання 9

a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))

count_integers = 0

if a == int(a):
    count_integers += 1
if b == int(b):
    count_integers += 1
if c == int(c):
    count_integers += 1

print("Кількість цілих чисел серед a, b, c:", count_integers)
