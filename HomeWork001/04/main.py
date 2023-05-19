# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

widht = int(input('Write widht - '))
height = int(input('Write height - '))
k = int(input('Write k - '))

if (k % widht == 0 or k % height == 0) and k < widht * height:
    print('yes')
else:
    print('no')
