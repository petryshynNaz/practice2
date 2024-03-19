# Завдання 6
a = int(input("Введіть ціле число a: "))
b = int(input("Введіть ціле число b: "))


if a != b:
    replacement = max(a, b)
    a = replacement
    b = replacement
else:
    a = 0
    b = 0


print("Після обробки:")
print("a =", a)
print("b =", b)
