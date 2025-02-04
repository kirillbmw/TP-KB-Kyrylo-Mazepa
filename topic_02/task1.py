import math

def find_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

def find_roots(a, b, c):
    D = find_discriminant(a, b, c)
    
    if D > 0:
        # Два різних дійсних корені
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return x1, x2
    elif D == 0:
        # Один дійсний корінь
        x = -b / (2*a)
        return x,

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

# Виклик функції та виведення результату
roots = find_roots(a, b, c)

if len(roots) == 1:
    print(f"Корінь рівняння: {roots[0]}")
else:
    print(f"Корені рівняння: {roots[0]} і {roots[1]}")
