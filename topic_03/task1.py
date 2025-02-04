# Операції калькулятора
def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else "Помилка: ділення на нуль!"
    return "Невідома операція!"

# Основна функція
def run_calculator():
    while True:
        # Введення першого числа або вихід
        num1_input = input("Введіть перше число або 'q' для виходу: ").lower()
        if num1_input == 'q':
            print("Програма завершена.")
            break

        try:
            num1 = float(num1_input)
        except ValueError:
            print("Помилка: введіть коректне число.")
            continue

        # Введення другого числа або вихід
        num2_input = input("Введіть друге число або 'q' для виходу: ").lower()
        if num2_input == 'q':
            print("Програма завершена.")
            break

        try:
            num2 = float(num2_input)
        except ValueError:
            print("Помилка: введіть коректне число.")
            continue

        # Введення операції
        operation = input("Оберіть операцію (+, -, *, /): ")
        if operation.lower() == 'q':
            print("Програма завершена.")
            break

        # Результат обчислення
        result = calculate(num1, num2, operation)
        print("Результат:", result)

# Запуск програми
run_calculator()
