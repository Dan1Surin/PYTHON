# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность
# и количество элементов нужно ввести с клавиатуры. Формула для получения n-го
# члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


a1=int(input('Write a1 '))
d=int(input('Write d '))
lenght=int(input('Write lenght '))

list_progress=[a1]

print(list_progress)

for i in range(lenght-1):
    list_progress.append(a1+(i-1)*d)

print(list_progress)