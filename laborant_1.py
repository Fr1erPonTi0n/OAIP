print('1 ЗАДАНИЕ')
print('Вводите название фильма, название кинотеатра и время\n ↓↓↓')
print(f'Билет на "{input()}" в "{input()}" на {input()} забронирован.')

print()
print('2 ЗАДАНИЕ')
cash_mount = int(input('Зарплата за месяц: \n>>> '))
count_hours = int(input('Количество отработанных в выходные часов: \n>>> '))
print(f'Размер премии: {(cash_mount * 0.01) * count_hours}')

print()
print('3 ЗАДАНИЕ')
n = int(input('Введите сумму: \n>>> '))
n1 = n // 1000
n2 = (n % 1000) // 100
n3 = (n % 100) // 10
n4 = (n % 10) // 1
print(n4, '- по 1р')
print(n3, '- по 10р')
print(n2, '- по 100р')
print(n1, '- по 1000р')

print()
print('4 ЗАДАНИЕ')
text = input('Оцените развлекательный комплекс:\n>>> ')
corret_words = ['весело', 'увлекательно', 'развлечения']
corret_numbers = []
for i in range(len(corret_words)):
    corret_numbers.append(text.find(corret_words[i]))
print('Результат анализа:', *corret_numbers, sep=' ')

print()
print('5 ЗАДАНИЕ')
text = input('Введите слово:\n>>> ')
if len(text) % 2 != 0:
    print(f'Средняя буква: {text[len(text) // 2]}')
else:
    print(f'Средняя буква: {text[(len(text) // 2) - 1]}')

print()
print('6 ЗАДАНИЕ')
feedback = 'Алиса и Вася, большое спасибо за теплый приём!'
name1 = feedback[:5]
name2 = feedback[8:12]
print(f'Назначить премию: {name1}/{name2}')

print()
print('7 ЗАДАНИЕ')
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input('Введите число:\n>>> '))
print_words = [chr(ord('A') + (n + i) % 26) for i in range(-1, 3)]
print('Буквы: ', *print_words, sep='')

print()
print('8-11 ЗАДАНИЯ')
print('--list().start()--')
list = list()
print(list)
print('Создать список')
print('-----')
list.append(1)
list.append(2)
list.append(3)
list.append(4)
print(list)  # [1, 2, 3, 4]
print('Добавить элементы')
print('-----')
list.pop(0)
print(list)  # [2, 3, 4]
print('Удалить элемент')
print('-----')
print(list[1:3])  # [3, 4]
print('Сделать срез')
print('-----')
list2 = []
for i in reversed(list):
    list2.append(i)
print(list2)  # [4, 3, 2]
print('Перевернуть список (1 способ)')
print('-----')
print(list[::-1])  # [4, 3, 2]
print('Перевернуть список (2 способ)')
print('-----')
list = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(list)  # [[1, 2], [3, 4], [5, 6], [7, 8]]
print('Сделать двумерный список')
print('-----')
print(list[0])  # [1, 2]
print('Работа с индексации двумерного списка (1)')
print('-----')
print(list[1][1])  # 4
print('Работа с индексации двумерного списка (2)')
print('-----')
list.clear()
print(list)  # []
print('Очистить список')
print('--list().end()--')

print()
print('--tuple().start()--')
print(())  # ()
print('Создание пустого кортежа')
print('-----')
print((1, 2, 3, "hello", True))  # (1, 2, 3, 'hello', True)
print('Создание заполненого кортежа')
print('--tuple().end()--')

print()
print('--set().start()--')
seta = set()
print(set())  # set()
print('Создание пустого множества')
print('-----')
sets = {'12', '45'}
print(sets)  # {'12', '45'}
print('Создание множества с элементами')
print('-----')
seta.add('123')
seta.add('123')
seta.add('44')
seta.add('55')
print(seta)  # {'44', '123', '55'}
print('Добавить в пустое множество элементы')
print('-----')
print(set([1, 2, 3, 2, 1]) == {3, 1, 2})  # True
print('Выполнить основные операции с множествами (1)')
print('-----')
print(seta | sets)  # {'12', '45', '123', '44', '55'}
print('Выполнить основные операции с множествами (2)')
print('-----')
print(seta & sets)  # set()
print('Выполнить основные операции с множествами (3)')
print('-----')
print(seta - sets)  # {'123', '44', '55'}
print('Выполнить основные операции с множествами (4)')
print('-----')
print(seta ^ sets)  # {'55', '44', '12', '45', '123'}
print('Выполнить основные операции с множествами (5)')
print('--set().end()--')

print()
print('--dict().start()--')
empty_dict = {}
print(empty_dict)  # {}
print('Создание пустого словаря')
print('-----')
my_dict = {"name": "Иван", "age": 30, "city": "Москва"}
print(my_dict)  # {'name': 'Иван', 'age': 30, 'city': 'Москва'}
print('Создание словаря с элементами')
print('-----')
my_dict["profession"] = "программист"
print(my_dict)  # {'name': 'Иван', 'age': 30, 'city': 'Москва', 'profession': 'программист'}
print('Добавить значение')
print('-----')
del my_dict["age"]
print(my_dict)  # {'name': 'Иван', 'city': 'Москва', 'profession': 'программист'}
print('Удалить значение')
print('-----')
my_dict["city"] = "Санкт-Петербург"
print(my_dict)  # {'name': 'Иван', 'city': 'Санкт-Петербург', 'profession': 'программист'}
print('Изменить значение')
print('--dict().end()--')
