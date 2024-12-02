def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('Ошибка: Число должно быть целочисленным')


def get_division(num1, num2):
    while True:
        try:
            result_div = num1 / num2
            return result_div
        except ZeroDivisionError:
            print('Ошибка: Нельзя делить на 0')
            break


try:
    n1 = get_integer("Первое число: ")
    n2 = get_integer("Второе число: ")

    result = n1 + n2
    print(f"Результат сложения: {result}")

    if get_division(n1, n2) is not None:
        print(f"Результат деления: {get_division(n1, n2)}")

except Exception:
    print('Неизвестная ошибка')

finally:
    print('Выход из программы')
  
