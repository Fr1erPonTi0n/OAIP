import math


def approximate_value(x, flag):
    s, a, n = 1, x, 1
    if flag:    # УСТОЙЧИВЫЙ АЛГОРИТМ (НЕ СДЕЛАН)
        while s + a != s:
            s += a
            n += 1
            a = a * (x / n)
    else:       # НЕУСТОЙЧИВЫЙ АЛГОРИТМ (СДЕЛАН)
        while s + a != s:
            s += a
            n += 1
            a = a * (x / n)
    return s


nums = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]

print('НЕУСТОЙЧИВЫЙ АЛГОРИТМ')
for elem in nums:
    num1 = approximate_value(elem, False)
    num2 = math.exp(elem)
    num3 = abs(num2 - num1) / num2
    print(f"{f'x = {elem}':<15} {f's = {num1}':<30} {f'math_exp = {num2}':<40} {f'Δ = {num3}':<35}")
print('УСТОЙЧИВЫЙ АЛГОРИТМ')
for elem in nums:
    num1 = approximate_value(elem, True)
    num2 = math.exp(elem)
    num3 = abs(num2 - num1) / num2
    print(f"{f'x = {elem}':<15} {f's = {num1}':<30} {f'math_exp = {num2}':<40} {f'Δ = {num3}':<35}")

