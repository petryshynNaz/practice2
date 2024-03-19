# Завдання 4

x = float(input("Введіть число x: "))
y = float(input("Введіть число y: "))

if x != y:

    if x < y:
        x = (x + y) / 2
        y = 2 * x
    else:
        y = (x + y) / 2
        x = 2 * y

    print("Після обробки:")
    print("x =", x)
    print("y =", y)
else:
    print("Числа не повинні бути рівні одне одному.")
