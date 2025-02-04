from functions import add, subtract, multiply, divide
from operations import get_first_number, get_second_number, get_operation

def calculator():
    while True:
        num1 = get_first_number()
        if num1 is None:
            break

        num2 = get_second_number()
        if num2 is None:
            break

        # Вибір операції
        while True:
            operation = get_operation()
            if operation is None:
                return 

            # Обробка операцій
            match operation:
                case '+':
                    print("Результат:", add(num1, num2))
                    break
                case '-':
                    print("Результат:", subtract(num1, num2))
                    break
                case '*':
                    print("Результат:", multiply(num1, num2))
                    break
                case '/':
                    result = divide(num1, num2)
                    if result is not None: 
                        print("Результат:", result)
                        break
                    else:
                        continue  # Запитуємо операцію знову
calculator()
