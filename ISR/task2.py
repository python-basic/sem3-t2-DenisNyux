"""
Nyukhalov Denis
IVT 2 kurs, group 3
"""
"""Значения в таблице истинности"""
values = ((0, 0), (0, 1), (1, 0), (1, 1))
header = '| A | B | F = (A∨B)∧(¬A∨¬B) |'
line = '+ ' + '-' * (len(header) - 4) + ' +'


def logical_operation(val):
    """Строит строки для таблицы истинности четвертого выражения"""
    log_expr =' F =(A∨B)∧(¬A∨¬B) '
    result = (val[0] or val[1]) and (not val[0] or not val[1])
    result = int(result)
    val_line = '| ' + str(val[0]) + ' | ' + str(val[1]) + ' | ' + str(result).center(len(log_expr)-1) + ' |'
    print(val_line, line, sep='\n')
    return result


def main():
    """Вывод таблицы"""
    print('\n4) F = (A∨B)∧(¬A∨¬B)', line, header, line, sep='\n')
    result = dict()
    for i in values:
        result.update({'input' + str(i): logical_operation(i)})
    print(result)


main()
