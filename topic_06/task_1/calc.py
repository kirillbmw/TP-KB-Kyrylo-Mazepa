from log import makeLog
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

        while True:
            operation = get_operation()
            if operation is None:
                return 

            if operation not in ('+', '-', '*', '/'):
                error_message = f"Unknown operation: {operation}. Please try again."
                print(error_message)
                makeLog(num1, operation, num2, error_message)  # Логування помилки
                continue  # Запитуємо операцію знову

            # Обробка операцій
            match operation:
                case '+':
                    result = add(num1, num2)
                    print("Result:", result)
                    makeLog(num1, operation, num2, result)
                    break
                case '-':
                    result = subtract(num1, num2)
                    print("Result:", result)
                    makeLog(num1, operation, num2, result)
                    break
                case '*':
                    result = multiply(num1, num2)
                    print("Result:", result)
                    makeLog(num1, operation, num2, result) 
                    break
                case '/':
                    result = divide(num1, num2)
                    if result is not None: 
                        print("Result:", result)
                        makeLog(num1, operation, num2, result) 
                        break
                    else:
                        makeLog(num1, operation, num2, "Error: division by zero!")  
                        continue  # Запитуємо операцію знову

calculator()
