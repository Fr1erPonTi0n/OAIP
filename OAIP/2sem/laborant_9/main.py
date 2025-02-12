from chest import Chest

def chest():
    exam = Chest()
    print(f"Вы видите сундук типа: {exam.get_rarity()}.")
    while True:
        print()
        print("Что вы хотите c ним сделать?")
        print("(1) Попытаться открыть сундук.")
        print("(2) Открыть сундук или вскрыть сундук.")
        print('(3) Закрыть на ключ сундук.')
        print("(4) Добавить предмет из инвентаря в сундук.")
        print("(5) Взять предмет из сундука в инвентарь.")
        print("(6) Открыть инвентарь игрока.")
        print("(7) Уйти.")
        try:
            choice_chest = int(input(">\t"))
        except ValueError:
            print('Введено значение, которое не является числом.')
            continue
        print()
        if choice_chest == 1:
            exam.open_chest()
        elif choice_chest == 2:
            exam.pick_lock()
        elif choice_chest == 3:
            exam.close_chest()
        elif choice_chest == 4:
            exam.input_item()
        elif choice_chest == 5:
            exam.get_item()
        elif choice_chest == 6:
            exam.open_player_inventor()
        elif choice_chest == 7:
            print('Ты уходишь от сундука, удачного приключения!')
            print()
            return

        else:
            print('Ты ввёл неправильное число!')



if __name__ == "__main__":
    while True:
        print('Какой класс запустить?')
        print('(1) Класс сундук')
        print('(2) Класс кнопка')
        print('(3) Класс питомец')
        print('(4) Выход')
        try:
            choice = int(input(">\t"))
        except ValueError:
            print('Введено значение, которое не является числом.')
            continue
        print()
        if choice == 1:
            chest()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            print('Выход')
            break
        else:
            print('Ты ввёл неправильное число!')