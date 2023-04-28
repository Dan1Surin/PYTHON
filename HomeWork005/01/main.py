# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит
# число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def degree(a, b):
    if b == 1: return a
    return degree(a, b - 1)*a

print('to raise a in degree b')
num_1 = int(input('write a - '))
num_2 = int(input('write b - '))

print(degree(num_1, num_2))
