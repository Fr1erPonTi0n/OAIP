#  1 ЗАДАНИЕ


def eight_print():
    numbers = []
    for i in range(8):
        numbers.append(input())
    return ''.join(numbers)


#  2 ЗАДАНИЕ


def order_of_people():
    people = []
    lista = []
    for i in range(int(input())):
        people.append(input())
    for i in range(len(people)):
        lista.append(f'{i + 1} {people[i]}')
    return '\n'.join(lista)


#  3 ЗАДАНИЕ


def timbykto():
    a = int(input())
    b = int(input())
    times_line = [str(a)]
    while a + b <= 31:
        a += b
        times_line.append(str(a))
    return ' '.join(times_line)


#  4 ЗАДАНИЕ


def max_letter():
    char = input()
    length = int(input())
    text = input()
    while True:
        if (text.find(char * length) != -1) or (length == 0):
            return length
        length += -1


#  5 ЗАДАНИЕ


def div():
    a = int(input())
    b = 1
    c = 0
    while b <= a:
        if a % b == 0:
            c += b
        b += 1
    return c


#  6 ЗАДАНИЕ


def russia_lang():
    text = input()
    count = 0
    for i in range(len(text)):
        if text[i] in 'аяоёэеуюыи':
            count += 1
    return count


#  7 ЗАДАНИЕ


def n_words():
    word = input()
    words = []
    for i in range(int(input())):
        words.append(word)
    return '\n'.join(words)


#  8 ЗАДАНИЕ


def nomer():
    number = input()
    for i in range(len(number)):
        if number[i] not in '+1234567890':
            return 'Неправильно номер телефона!'
    return 'Bce ok!'


#  9 ЗАДАНИЕ


def russia_password():
    vowels = 'аеёиоуыэюя'
    consonants = 'бвгджзйклмнпрстфхцчшщъь'
    login = input().lower()
    task = []
    for i in login:
        if i in vowels:
            task.append('0')
        else:
            task.append('1')
    return ''.join(task)


#  10 ЗАДАНИЕ


def debug_text():
    message = input()
    output = []
    last_letter = ''
    for i in range(len(message)):
        if last_letter != message[i]:
            output.append(message[i])
        last_letter = message[i]
    return ''.join(output)
