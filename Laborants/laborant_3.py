#  1 ЗАДАНИЕ


def count_str():
    text = input()
    count = 0
    while text != '':
        count += 1
        text = input()
    return count


#  2 ЗАДАНИЕ


def count_num():
    num = float(input())
    count = 0
    while num < 36.6:
        if num < 0:
            count += 1
            num = float(input())
        else:
            num = float(input())
    return count


#  3 ЗАДАНИЕ


def second_max():
    return 'НЕ СДЕЛАНО'


#  4 ЗАДАНИЕ


def min_num(n=str):
    lista = n.split(' ')
    maxa = 0
    for i in range(len(lista)):
        if int(lista[i]) > maxa:
            maxa = int(lista[i])
        else:
            continue
    return maxa


#  5 ЗАДАНИЕ


def check_num(n=int):
    if (n % 7 == 0) and (n % 2 == 0):
        return 'Караул!'
    elif n % 2 == 0:
        return 'несчастливое'
    elif n % 7 == 0:
        return 'опасное'
    else:
        return 'нормальное'


#  6 ЗАДАНИЕ


def IsPrime(n=int):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def sum_num():
    n = 0
    for i in range(2, 10001):
        if IsPrime(i):
            n += i
        else:
            continue
    return n


#  7 ЗАДАНИЕ


def comparison(x1, y1, z1, x2, y2, z2):
    if x1 > x2 and y1 > y2 and z1 > z2:
        return 'Да'
    else:
        return 'Нет'


#  8 ЗАДАНИЕ


def read_str():
    text = input()
    min_text = ''
    while text != 'стоп':
        if min_text == '':
            min_text = text[:]
            text = input()
        elif len(text) < len(min_text):
            min_text = text[:]
            text = input()
        else:
            text = input()
            continue
    return min_text


#  9 ЗАДАНИЕ


def calculator():
    nums = [input()]
    while nums[-1] != 'стоп':
        nums.append(input())
    return eval(' '.join(nums[:-1]))


#  10 ЗАДАНИЕ


def text():
    nums = [input()]
    n = 0
    texta = []
    output = []
    while nums[-1] != 'стоп':
        nums.append(input())
    nums.remove('стоп')
    for i in range(len(nums)):
        if nums[i] == '!':
            output.append(f'{" ".join(texta)}{"!"}')
            texta = []
        else:
            texta.append(nums[i])
    return '\n'.join(output)