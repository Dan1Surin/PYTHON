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

for i in range(len(list_1)):
    if list_1[i]>=min and list_1[i]<=max:
        list_index.append(i)

print(list_1)
print(list_index)