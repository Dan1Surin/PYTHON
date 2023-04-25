# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов
# второго множества. Затем пользователь вводит сами элементы множеств.
import random

n=int(input('Write number of elements n = '))
m=int(input('Write number of elements m = '))
list_n = {random.randint(0,10) for _ in range(n)}
list_m = {random.randint(0,10) for _ in range(m)}

print(list_n,list_m)
print(*list_n & list_m)


