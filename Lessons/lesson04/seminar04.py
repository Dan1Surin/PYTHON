### Семинар 4
# На вход строку, отслеживает сколько раз символ уже встречался,
# количество пофторов добавляется при помощи
# постфикса формата _n

my_string=list(input("Write string"))
#
# print(my_string[0],end=" ")
# for i in range(1,len(my_string)):
#     print(f"{my_string[i]}", end=" ")
#     count=my_string[:i-1].count(my_string[i]) ##срез строки до элемента
#     if count >0:
#         print(f"_{count}",end=" ")

## Вариант с использованием словаря(ключом будет буква)

count_dict = {}
for letter in my_string:
    count_dict[letter] = count_dict.get(letter, 0)+1
    #print(letter,count_dict[letter])
    ##вывод значения, перед перезаписью/ если значение none по ключу, выдаст 0(get(none,0)
    print(f'{letter}' if count_dict.get(letter) ==1  else f'{letter}_{count_dict.get(letter)}',end=' ')




