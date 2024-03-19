# Завдання 7

a = int(input("Введіть ціле число a: "))
b = int(input("Введіть ціле число b: "))
c = int(input("Введіть ціле число c: "))

count_negative = 0

if a < 0:
    count_negative += 1
if b < 0:
    count_negative += 1
if c < 0:
    count_negative += 1

print("Кількість негативних чисел серед a, b, c:", count_negative)
