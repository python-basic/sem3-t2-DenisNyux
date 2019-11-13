"""
Nyukhalov Denis
IVT 2 kurs, group 3
"""
"""Значения в таблице истинности"""
values = ((0, 0), (0, 1), (1, 0), (1, 1))


def head():
    """Выводит 'шапку' таблицы"""
    header = '| A | B | F |'
    under_header = '+ ' + '-' * (len(header) - 4) + ' +'
    print(under_header)
    print(header)
    print(under_header)


def logical_operation(val):
    """Строит строки для таблицы истинности четвертого выражения"""
    result = (val[0] or val[1]) and (not val[0] or not val[1])
    result = int(result)
    line = '| ' + str(val[0]) + ' | ' + str(val[1]) + ' | ' + str(result) + ' |'
    print(line)
    print('+', '-' * (len(line)-4), '+')
    return result


def main():
    """Вывод таблицы"""
    print('\n4) F = (A∨B)∧(¬A∨¬B)\n')
    head()
    result = dict()
    for i in range(len(values)):
        result.update({'input' + str(values[i]): logical_operation(values[i])})
    print(result)


main()
