# Завдання 1
def square_power(x):
    if x >= 0:
        return x ** 2
    else:
        return x ** 4


a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

result_a = square_power(a)
result_b = square_power(b)
result_c = square_power(c)

print("Результат для першого числа:", result_a)
print("Результат для другого числа:", result_b)
print("Результат для третього числа:", result_c)
