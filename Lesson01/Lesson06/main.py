# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

def message(str):
    a = int(input(str))
    return a


from random  import randint
def random_list(min,max,list_lenght):
        a=[randint(min,max) for i in range(list_lenght)]
        return a

list_1=random_list(message('введите min '),message('введите max '),message('введите lenght '))
list_2=random_list(message('введите min '),message('введите max '),message('введите lenght ')-1)
print(list_1)
print(list_2)
