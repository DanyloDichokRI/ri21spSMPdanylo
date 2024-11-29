import math


memory = None


history = []



def get_input():
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
        if operator != '√':
            num2 = float(input("Введіть друге число: "))
        else:
            num2 = None
        return num1, operator, num2
    except ValueError:
        print("Помилка: введено некоректне значення.")
        return get_input()



def valid_operator(operator):
    return operator in ['+', '-', '*', '/', '^', '√', '%']



def calculate(num1, operator, num2):
    global memory
    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль неможливе.")
            result = num1 / num2
        elif operator == '^':
            result = num1 ** num2
        elif operator == '√':
            if num1 < 0:
                raise ValueError("Корінь із від'ємного числа неможливий.")
            result = math.sqrt(num1)
        elif operator == '%':
            result = num1 % num2
        else:
            raise ValueError("Невідомий оператор.")


        memory = result


        history.append(f"{num1} {operator} {num2 if num2 is not None else ''} = {result}")

        return result
    except ZeroDivisionError as e:
        print(f"Помилка: {e}")
        return None
    except ValueError as e:
        print(f"Помилка: {e}")
        return None



while True:
    num1, operator, num2 = get_input()

    if not valid_operator(operator):
        print("Невірний оператор. Спробуйте ще раз.")
        continue

    result = calculate(num1, operator, num2)
    if result is not None:
        print(f"Результат: {result}")


    next_step = input("Бажаєте продовжити обчислення? (так/ні): ").strip().lower()
    if next_step != 'так':

        view_history = input("Бажаєте переглянути історію обчислень? (так/ні): ").strip().lower()
        if view_history == 'так':
            print("\nІсторія обчислень:")
            for record in history:
                print(record)
        break
