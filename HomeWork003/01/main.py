# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в
# массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка
# содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random

size = 25
num = [random.randint(0,100) for _ in range(size)]
print(*num)

count=0 ## счётчик
a=1 ##переменная для поиска ближайшего числа
num_1=0 ##переменная для вывода ближайшего числа

x = int(input('Введите искомое число X - '))
for i in num:# count = num.count(x)
    if i==x:
        count+=1
if count>0:
    print(f'число встречается - {count} раз')
else:
    for i in num:
        if abs(i-x)==a:
            num_1=i
        else:
            a+=1
    print(f'ближайшее число - {num_1}')





