def func_table(f, x_max, y_max):
    for y in range(y_max + 1):
        row = []
        for x in range(x_max + 1):
            result = eval(f)
            row.append(str(result))
        print('\t'.join(row))
