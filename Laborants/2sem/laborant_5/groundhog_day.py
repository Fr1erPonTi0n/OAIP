def groundhog_day(strings):
    for i in range(1, len(strings)):
        current_string = strings[i]
        previous_string = strings[i - 1]
        if len(current_string) != len(previous_string):
            continue
        differences = sum(1 for a, b in zip(current_string, previous_string) if a != b)
        if differences > 2:
            differing_indices = [index for index in range(len(current_string)) if
                                 current_string[index] != previous_string[index]]
            return (i, *differing_indices)
    return (0, 0)
