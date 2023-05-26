### Функции
##def вызов функции
def sum_numbers(n, y = 'Hello'): ##У значение по умолчанию, которое можно заменить при вызове функции
    summa=0
    print(y)
    for i in range(1,n+1):
        summa+=i
    return summa


### передаем неограниченное колличество аргументов(заранее неизвестно колличество)

def sum_str(*args):
    res=''
    for i in args:
        res +=i
    return res

#print(sum_str('w','e','gg','e'))
#print(sum_str(1,2,3,4))

###Модульность
#множество функций в другом файле
# импортировать можно функцией import имя_файла
# применить имя_файла.имя_функции

import modul11

print(modul11.max(2,6))

# from modul11 import max ##импорт конкретной функции

# from modul11 import * ##импорт всех функции

import modul11 as m1

print(m1.max(11,6))

### Рекурсия
def fib(n):
    if n in [1,2]: return 1 ### базис рекурсии(когда закончить)
    return fib(n-1)+fib(n-2)

list_1=[]
for i in range(1,10):list_1.append(fib(i))
print(list_1)

###Быстрая сортировка

def quick_sort(list1):
    if len(list1) <= 1: ### базис рекурсии(когда закончить)
        return  list1
    else:
        pivot=list1[0]
        less=[i for i in list1[1:] if i <= pivot]
        greater=[i for i in list1[1:] if i> pivot]
        return quick_sort(less)+ [pivot] + quick_sort(greater)

print(quick_sort([1,4,5,7,8,5,2,4,6,7,8,4,2,4,5,6]))

### Сортировка слиянием

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
        nums[k] = left[i]
        i += 1
    else:
        nums[k] = right[j]
        j += 1
        k += 1
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1
        nums = [38, 27, 43, 3, 9, 82, 10]
        merge_sort(nums)
    print(nums)