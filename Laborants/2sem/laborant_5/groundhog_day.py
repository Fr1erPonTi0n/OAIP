def groundhog_day(strings):
    for i in range(1, len(strings)):
        current_string = strings[i]
        previous_string = strings[i - 1]
        if len(current_string) != len(previous_string):
            continue
        differences = 0
        length = max(len(current_string), len(previous_string))
        for j in range(length):
            a = current_string[j] if j < len(current_string) else None
            b = previous_string[j] if j < len(previous_string) else None
            if a != b:
                differences += 1
        if differences > 2:
            differing_indices = [index for index in range(len(current_string)) if
                                 current_string[index] != previous_string[index]]
            return i, *differing_indices
    return 0, 0
