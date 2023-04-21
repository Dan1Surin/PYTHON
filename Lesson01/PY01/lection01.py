# за день машина проезжает n
# сколько дней нужно чтобы проехать m

# n = int(input('write n  '))
# m = int(input('write m  '))
#
# print(f"Days {round(m/n,0)}")
#
# print((m+n-1)//n)

##если нужно проехать 2 км а за день 10
##то округление некоректно

##три класса сколько нужно минимальное колличество парт

# a=int(input('введите колличество учеников'))
# b=int(input('введите колличество учеников'))
# c=int(input('введите колличество учеников'))
#
# print((a+1)//2+(b+1)//2+(c+1)//2)   ##целочисленное деление, округление не работате

# print(5)

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

# text = 'I want to break free'
# print(len(text))### len количество символов
# print('want' in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('I','You'))

# print(text[:4])
# print(text[1:20:2])

