# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
# за проезд и получали
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме
# последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no


## решение строками

n = int(input('Номер билета(строками) - '))
if (n < 100000 or n > 999999):
    print('странный номер')
else:
    n = str(n)
    if (int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5])):
        print('Счастливый')
    else:
        print('не повезло')

## решение арифметически

n = int(input('Номер билета(арифметически) - '))
if (n < 100000 or n > 999999):
    print('странный номер')
else:
    l = n // 1000
    r = n % 1000
    if (l / 100 + (l % 100) + (l % 10 / 10) == r / 100 + (r % 100) + (r % 10 / 10)):
        print('Счастливый')
    else:
        print('не повезло')
