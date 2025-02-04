# Функції для операцій
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Помилка: ділення на нуль!")
        return None
    return a / b

# Основна функція калькулятора
def calculator():
    while True:
        # Введення першого числа
        user_input = input("Введіть перше число або 'q': ")
        if user_input.lower() == 'q':
            print("Програма завершена.")
            break
        try:
            num1 = float(user_input)
        except ValueError:
            print("Помилка: введіть коректне число.")
            continue

        # Введення другого числа
        user_input = input("Введіть друге число або 'q': ")
        if user_input.lower() == 'q':
            print("Програма завершена.")
            break
        try:
            num2 = float(user_input)
        except ValueError:
            print("Помилка: введіть коректне число.")
            continue

        # Вибір операції
        operation = input("Оберіть операцію (+, -, *, /): ")
        if operation.lower() == 'q':
            print("Програма завершена.")
            break

        # Виконання операції через match-case
        match operation:
            case '+':
                print("Результат:", add(num1, num2))
            case '-':
                print("Результат:", subtract(num1, num2))
            case '*':
                print("Результат:", multiply(num1, num2))
            case '/':
                result = divide(num1, num2)
                if result is not None:
                    print("Результат:", result)
            case _:
                print("Невідома операція. Спробуйте ще раз.")

calculator()
