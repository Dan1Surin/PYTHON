# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Write n - '))
m = int(input('Write m - '))
k = int(input('Write k - '))

if(n>m):
    if(round(n / 2)*m >= k):
        print('yes')
    else:
        print('no')
else:
    if((round(m / 2)*n) >= k):
        print('yes')
    else:
        print('no')



