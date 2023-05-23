### Функции высшего порядка

## Функция в функции

def calk(a, b):
    return a + a


def math(op, x, y):
    print(op(x, y))


# math(lambda a,b:a+b,3,5)

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = list()


def simple(data, res):
    for i in data:
        if i % 2 == 0:
            res.append((i, i ** 2))
    print(res)


# simple(data,res)

## select возвращает элементы списка к которым применили функцию f(любую которуб передали при вызове)
def select(f, col):
    return [f(x) for x in col]  # возвращает список[]


# возвращает только то что попадает под условия заданной функции f
def where(f, col):
    return [x for x in col if f(x)]


res = select(int, data)
# print(res)
res = where(lambda x: x % 2 == 0, res)
# print(res)
res = list(select(lambda x: (x, x ** 2), res))
# print(res)


## функция map то же что мы делали в функции select
# только в одну строку,
# принимает значение и функцию которую надо применить к значению

list_1 = [x for x in range(1, 20)]
# print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))

# print(list_1)

# .split() преобразует строку в список строк(указывает разделитель)

data1 = '15 34 23 656 78 8 9 0 544 3'

# data1=data1.split()
# print(data1)

data1 = list(map(int, data1.split()))
print(data1)

## Функция фильтр принимает функцию и значение
# (возвращает только то что при вызове функции вернет занчение true)

data2 = [12, 34, 567, 15, 23, 175, 5, 231, 25]
res1 = list(filter(lambda x: x % 10 == 5, data2))
print(res1)

# zip склеивает элементы на одной позиции из заданных списков выводя кортеж

users = ['us1', 'us2', 'us3']
ids = [4, 3, 4, 6, 7]
data11 = list(zip(users, ids))
print(data11)

# enumerate выводит порядковый номер

users = ['us1', 'us2', 'us3']
data11 = list(enumerate(users))
print(data11)

###isdigit если число
list_111 = ['2', 'wee', '2', 'qe', '22', '1', '23']

list_111 = list(filter(lambda x: x.isdigit(), list_111))
print(list_111)


## кусок практики

def same_by(characteristic, objects):
    my_set = set(map(characteristic, objects))
    print(my_set)
    return len(my_set) < 2


my_list = [2, 3, 5, 6, 4]
print(same_by(lambda x: x % 2, my_list))
