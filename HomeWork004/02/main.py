
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод
# — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из
# управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n=int(input('write n'))
list_n=[]
for i in range(n):
    x = int(input('x'))
    list_n.append(x)

list_n_count=[]
for i in range(len(list_n)-1):
    list_n_count.append(list_n[i-1]+list_n[i]+list_n[i+1])
list_n_count.append(list_n[-2]+list_n[-1]+list_n[0])
print(max(list_n_count))