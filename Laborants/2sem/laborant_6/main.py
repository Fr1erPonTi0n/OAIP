from quaters import quaters


def main():
    data = [(1, 1), (-1, 2), (-3, -1)]
    for k, v in sorted(quaters(*data).items()):
        print(f'{k}:\t{v}')
    data = [(-5, 1), (-1, 3), (2, -1), (0, 3)]
    for k, v in sorted(quaters(*data).items()):
        print(f'{k}:\t{v}')


if __name__ == '__main__':
    main()