class Operations:
    def get_first_number(self):
        while True:
            user_input = input("Введіть перше число або 'q' для виходу: ")
            if user_input.lower() == 'q':
                print("Програму завершено.")
                return None
            try:
                return float(user_input)
            except ValueError:
                print("Помилка: Введено нечислове значення. Спробуйте ще раз.")

    def get_second_number(self):
        while True:
            user_input = input("Введіть друге число або 'q' для виходу: ")
            if user_input.lower() == 'q':
                print("Програму завершено.")
                return None
            try:
                return float(user_input)
            except ValueError:
                print("Помилка: Введено нечислове значення. Спробуйте ще раз.")

    def get_operation(self):
        while True:
            operation = input("Оберіть операцію (+, -, *, /) або 'q' для виходу: ")
            if operation.lower() == 'q':
                print("Програму завершено.")
                return None
            if operation in ('+', '-', '*', '/'):
                return operation
            print(f"Невідома операція: {operation}. Спробуйте ще раз.")