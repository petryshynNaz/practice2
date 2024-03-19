# Завдання 8

a = int(input("Введіть ціле число a: "))
b = int(input("Введіть ціле число b: "))
c = int(input("Введіть ціле число c: "))

count_positive = 0

if a > 0:
    count_positive += 1
if b > 0:
    count_positive += 1
if c > 0:
    count_positive += 1

print("Кількість додатних чисел серед a, b, c:", count_positive)
