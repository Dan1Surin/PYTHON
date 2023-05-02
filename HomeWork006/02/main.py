# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random  import randint
def random_list(min,max,list_lenght):
        a=[randint(min,max) for i in range(list_lenght)]
        return a
def message(str):
    a = int(input(str))
    return a

min=message('min')
max=message('max')

list_1=random_list(1,100,10)
list_index=[]

for i in list_1:
    if min<list_1[i]>max:
        list_index.append(list_1[i])
    else:print('нет в списке')

print(list_index)