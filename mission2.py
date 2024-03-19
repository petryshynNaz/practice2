import math

# Завдання 2
x1 = float(input("Введіть координату x1 для точки A: "))
y1 = float(input("Введіть координату y1 для точки A: "))
x2 = float(input("Введіть координату x2 для точки B: "))
y2 = float(input("Введіть координату y2 для точки B: "))

distance_A = math.sqrt(x1**2 + y1**2)
distance_B = math.sqrt(x2**2 + y2**2)

if distance_A < distance_B:
    print("Точка A знаходиться ближче до початку координат.")
elif distance_A > distance_B:
    print("Точка B знаходиться ближче до початку координат.")
else:
    print("Точки A і B знаходяться на однаковій відстані до початку координат.")
