import math


def approximate_value(x):
    s = 1
    a = x
    n = 1
    while s + a != s:
        s += a
        n += 1
        a = a * (x / n)
    return s


nums = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]

print('НЕУСТОЙЧИВЫЙ АЛГОРИТМ')
for elem in nums:
    num1 = approximate_value(elem)
    num2 = math.exp(elem)
    num3 = abs(num2 - num1) / num2
    print(f"x = {elem}\t\ts = {num1}\t\tmath_exp = {num2}\t\tΔ = {num3}")

print('\nУСТОЙЧИВЫЙ АЛГОРИТМ')
for elem in nums:
    # num1 = approximate_value(elem)
    num2 = math.exp(elem)
    # num3 = abs(num1 - num2) / num1
    # print(f"x = {elem}\t\ts = {num1}\t\tmath_exp = {num2}\t\tΔ = {num3}")

