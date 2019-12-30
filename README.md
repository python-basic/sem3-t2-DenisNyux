<<<<<<< HEAD
# Самостоятельная работа по теме №2
## Нюхалов Денис, ИВТ2
=======
# Тема 5. Понятие функции, объявление функций

>>>>>>> 748100a0253e6fc8daf2617577069d51bfe94e47
### Инвариантная самостоятельная работа:
Задание 1:
```python
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
```
Задание 2:
```python
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

```
Задание 3:
```python
def sample(lst):
    lst8 = lst[len(lst) // 2 - 1::-2]
    sumof8 = sum(lst8)
    lst12 = lst[1:len(lst) // 2 + 1:2]
    sumof12 = sum(lst12)
    return [sumof8, sumof12]


def main():
    fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
    print(sample(fibs))


main()
```
Задание 4:
![att1](/ISR/task4_attachment1.png)

![att2](/ISR/task4_attachment2.png)
```python
from math import *


def square(d1, d2, h):
    a = sqrt((d1/2)**2 + (d2/2)**2)
    return a*a*2 + 4*a*h


def main():
    d1 = int(input('Введите первую диагональ: '))
    d2 = int(input('Введите вторую диагональ: '))
    h = int(input('Введите высоту призмы: '))
    print('Площадь поверхности призмы:', square(d1, d2, h))


main()

```
### Вариативная самостоятельная работа
Задание 1:

см. ISR/task1.docx

Задание 2:
```python
def two_line_function(vals):
    res = set(vals)
    return list(res)


def main():
    print('Введите количество значений: ', end='')
    i = int(input())
    values = list()
    while i != 0:
        values.append(input())
        i -= 1
    print('Введенные значения: ', values)
    print('Уникальные значения: ', two_line_function(values))


main()

```

Задание 3:
```python
a = [1, 2, 3]
b = [4, 5, 6]
c = 'abc'
res = tuple(map(lambda *args: args, a, b, c))
print(res)


```
