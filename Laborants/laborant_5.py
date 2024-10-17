#  1 ЗАДАНИЕ


def trafarets():
    nums = set()
    for i in range(int(input())):
        text = input()
        for j in range(len(text)):
            nums.add(text[j])
    return len(nums)


#  2 ЗАДАНИЕ


def set_words():
    word1, w1_set = input().upper(), set()
    word2, w2_set = input().upper(), set()
    word3, w3_set = input().upper(), set()
    words_intersection = []

    for i in range(len(word1)):
        w1_set.add(word1[i])
    for i in range(len(word2)):
        w2_set.add(word2[i])
    for i in range(len(word3)):
        w3_set.add(word3[i])

    words_intersection += w1_set.intersection(w2_set)
    words_intersection += w1_set.intersection(w3_set)
    words_intersection += w2_set.intersection(w3_set)

    return ''.join(sorted(set(words_intersection)))


#  3 ЗАДАНИЕ


def find_num():
    numbers = [int(num) for num in input()]
    not_find = []
    for i in range(1, 10):
        if i not in numbers:
            not_find.append(str(i))
    return ' '.join(not_find)


#  4 ЗАДАНИЕ


def posled_nums():
    nums = []
    n = int(input())
    while n != 0:
        nums.append(n)
        n = int(input())
    return [nums[i] for i in range(len(nums)) if nums[i] % len(nums) == 0]


#  5 ЗАДАНИЕ


def flags():
    flags = [input() for i in range(int(input()))]
    return '\n'.join([flags[i % len(flags)] for i in range(int(input()))])


#  6 ЗАДАНИЕ


def era_dinozavrov():
    pal = {
        "Proterozoic": range(635 * 10 ** 6, 2800 * 10 ** 6),
        "Cenozoic": range(0, 145 * 10 ** 6),
        "Mesozoic": range(145 * 10 ** 6, 300 * 10 ** 6),
        "Paleozoic": range(300 * 10 ** 6, 635 * 10 ** 6)
    }
    ers = []
    while True:
        x = input()
        if x == "":
            break
        x = int(x) * 1000
        for key, value in pal.items():
            if x in value:
                ers.append(key)
                break
        else:
            ers.append("Archaea")
    return '\n'.join(ers)


#  7 ЗАДАНИЕ


def angry_birds():
    output = {}
    bird = input()
    while bird != '':
        if bird.split(':')[0] not in output:
            output[bird.split(':')[0]] = int(bird.split(':')[1])
        else:
            output[bird.split(':')[0]] = int(bird.split(':')[1]) + int(output[bird.split(':')[0]])
        bird = input()
    return output


#  8 ЗАДАНИЕ


def binary_n_sys():
    nums = input().split()
    output = []
    for num in nums:
        binary_representation = bin(int(num))[2:]
        characteristics = {
            'digits': len(binary_representation),
            'units': binary_representation.count('1'),
            'zeros': binary_representation.count('0')
        }
        output.append(characteristics)
    return output
