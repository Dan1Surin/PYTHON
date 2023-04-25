import random

mark_list=[random.randint(1, 5) for _ in range(10)]
print(mark_list)
mark_list=[min(mark_list) if i == max(mark_list) else i for i in mark_list]
print(mark_list)


## Проверка является ли число простым(делится только на 1 и на себя)
def simp(a):
    number=int(input('Write number'))
    count=0
    for i in range(1,number+1):
        if number%i==0:
            count+=1
    if count==2: print('simple')
    else: print('not')


def is_simple(num:int) -> bool:
    if num in [1,2]: return True
    elif not num%2: return False
    for i in range(3,num//2+1,2):  ##оптимизация, поиск только  в половине и каждое нечетное
        if num%i==0: return False
    return True
num=int(input('number = '))
print(is_simple(num))
print(f'число '+('simple'if is_simple(num) else 'not'))