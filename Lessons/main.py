# print(5)
# import random

# # ctrl + f5 / p пуск ; ctrl + / -коммент выделенного участка - #
# # python3 -m venv .folder - создать виртуальное окружение, для выбора версий библиотек

# # int,float,bool,str - типы данных

# # Создать переменную можно с пустым значением для это присваиваем None

# '''\dsaf
# тоже коммит
# '''


# n = None

# print(n)

# n = "sdsdaff"

# print(type(n), n)

# a = 1111
# b = 3, 213
# c = "end"

# print(f"{n} - {a} --{c} ***{b}")

# print("{} -+ {} - {} - -- {}".format(a, n, b, c))  # функция формат


# # print("First number")

# # a = input()

# # print(a)

# # b = input('Second number')
# # print('b =', b)

# b=2
# a=5.33
# print(a,b,a+b)

# c=5.89
# print(type(c))
# c=int(c)    #Приведение типов - тут отбрасывается дробная часть
# print(type(c))

# c=5.3323
# b=3.2312
# print("summ",round(c*b,1)) #округление до 1 занака после запятой

# #сокращенная запись
# iter=1

# iter+=3
# print(iter)
# iter-=3
# print(iter)
# iter/=3
# print(iter)
# iter//=3
# print(iter)
# iter%=3
# print(iter)
# iter**=3 # в степень 5
# print(iter)


# a=1<4 and 5>2
# print(a)
# a=1==2 # равенство
# print(a)
# a=1!=2 # не равенство
# print(a)
# a="qwe"
# b="qwe"
# print(a==b)
# a=1<3<5<10
# print(a)

###IF ELSE ELIF

# username = int(input('Write name: '))
# if username == 1:
#     print('111111')
# elif username==2 and username>0:
#     print('22222')
# elif username==3 or username ==4:
#     print('3333444')
# else:
#     print('end')

###WHILE

# i=0
# while i<5:
#     if i == 3:
#         break
#     i=i+1
# else:
#     print('stop')
# print(i)

### FLAG

# n=int(input())
# flag=True
# i=2
# while flag: ### то же самое что flag==True:
#     if n%i==0:
#         flag=False
#         print(i)
#     elif i>n//2:
#         print(n)
#         flag=False
#     i +=1

###FOR

# for i in 1,2,3,4,5:
#     print(i*10)
    
# for i in range(0,20,2): ##(start,stop-1,step)
#     print(i*2)


# a="фывапро"  ###СТРОКИ
# for i in a:
#     print(i)

#  text = 'I want to break free'
#  print(len(text))### len количество символов
#  print('want' in text)
#  print(text.lower())
#  print(text.upper())
#  print(text.replace('I','You'))

#  print(text[:4])
#  print(text[1:20:2])

## Семинар 2

### Замена переменных, без использования третьей переменной

# n=1
# a=0
# n,a=a,n
#
# my_limit = int(input('введите предел факториала - '))
#
# fact = 1
# count = 1
# while count <= my_limit:
#     fact *= count
#     count += 1
# print(fact)

### FIBONACHI

# n1=0
# n2=1
# i=1
#
# num= int(input('Write edge'))
# while n2<num:
#     i+=1
#     n1,n2=n2,n1+n2
#     print(i)
# else:
#     print(-1)

## Тернарный оператор
## print(i if num == n2 else -1) сокращенная запись

### Максимальное колличество теплых дней подряд за месяц(>0)

# import random
#
# lenght=30
# count=0
# max_count=0
#
# for i in range(lenght): ### вместо while чтобы перебрать range
#     today = 0
#     today += random.randint(-3, 3)
#     print(today, end=" ") ### в одну строку
#     if today >= 0:
#         count += 1
#         if count>max_count:
#             max_count=count
#         else:
#             count=0
#     i+=1
# print(f"\n Максимальное число теплых дней {max_count}")  ### \n с новой строки

### Семинар 3

# дан список чисел, определите сколько в нем встречается различных чисел

# list_numbers = [1,1,2,3,4,54,65,6,66,66,7,8,9,3,1,23,4,5]
# # print(list_numbers)
# # list_uniq_numbers=set(list_numbers)
# # print(list_uniq_numbers)
# # print(len(list_uniq_numbers))

# list_num=list(input('Write list numbers')) # list - convert string to list
# print(list_num)
##решение в одну строку
# print(set_num := input('Write list numbers: '), len(set(set_num)))

#решение перебором
# uniq_list=[]
# for item in list_num:
#     if not item in uniq_list: ## проверка вхождения в коллекцию, список или строку
#         uniq_list.append(item)
# print(uniq_list)

# num = 5
# set_num={1,2,3,4,3,2,1} ## множество уникальных элементов set
# print(num in set_num) ## проверка вхождения, множество можно только перебрать

### список кортеж множество словари
# list[]     список
# tuple()     кортеж
# set{}       множество
# dict{key:value}     словарь

## сдвинуть на K элементы в списке

# k=int(input('введите число сдвига к - '))
# num_list=[1,2,3,4,5,6]
# for a in range(k):
#     num_list.insert(0,num_list.pop(-1)) ### не обязательно -1
# print(num_list)
#
# num_list = num_list[-k:] + num_list[:-k] ### срезами
#
# print(num_list)

### Работа со словорями
###Напишите программу для печати всех уникальных
###значений в словаре.

# my_list = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},
#            {"VI":"S005"},{"VII":"S005"},{" V ":"S009"},
#            {"VIII":"S007"}]### это список словарей
#
# uniq=set()
# for i in my_list:
#     print(i)
#     for value in i.values():### по словарю можно пройти циклом тремя способами keys,values,items
#         print(value)
#         uniq.add(value)
# print(uniq)
#
# модуль это abs(14-15)





