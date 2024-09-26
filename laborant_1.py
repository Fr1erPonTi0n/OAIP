#  1 ЗАДАНИЕ


def cinema(film, cinema,time):
    return f'Билет на "{film}" в "{cinema}" на {time} забронирован.'


#  2 ЗАДАНИЕ


def monthly_salary(cash_mount, count_hours)
    return f'Размер премии: {(cash_mount * 0.01) * count_hours}'


#  3 ЗАДАНИЕ


def cash_change(n):
    n1 = n // 1000
    n2 = (n % 1000) // 100
    n3 = (n % 100) // 10
    n4 = (n % 10) // 1
    print(n4, '- по 1р')
    print(n3, '- по 10р')
    print(n2, '- по 100р')
    print(n1, '- по 1000р')


#  4 ЗАДАНИЕ


def positive_feedback(text):
    corret_words = ['весело', 'увлекательно', 'развлечения']
    corret_numbers = []
    for i in range(len(corret_words)):
        if corret_words[i] in text:
            corret_numbers.append(text.find(corret_words[i]))
        else:
            continue
    return corret_numbers


#  5 ЗАДАНИЕ


def middle_letter(text):
    if len(text) % 2 != 0:
        return f'Средняя буква: {text[len(text) // 2]}'
    else:
        return f'Средняя буква: {text[(len(text) // 2) - 1]}'


#  6 ЗАДАНИЕ


feedback = 'Алиса и Вася, большое спасибо за теплый приём!'
name1 = feedback[:5]
name2 = feedback[8:12]
print(f'Назначить премию: {name1}/{name2}')


#  7 ЗАДАНИЕ

def four_letters_alphabet(n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print_words = [chr(ord('A') + (n + i) % 26) for i in range(-1, 3)]
    return 'Буквы: ', *print_words, sep='')
