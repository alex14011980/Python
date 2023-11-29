'''
Задача №41.Дан массив, состоящий из целых чисел.
Напишите программу, которая в данном массиве определит количество элементов,
у которых два соседних и, при этом, оба соседних элемента меньше данного.
Сначала вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
Ввод: 5   1 2 3 4 5   Вывод:  0                    Ввод:  5       1 5 1 5 1  Вывод:  2
(каждое число вводится с новой строки)
'''

def search_el(list_el):
    count = 0
    for i in range(1, len(list_el) - 1):
        if list_el[i] > list_el[i-1] and list_el[i] > list_el[i+1]:
            count += 1
    return count


list1 = [1, 6, 3, 6, 5, 7, 4]
print(search_el(list1))


my_set = set()
for el in range(10):
    my_set.add(el)


my_set = {el for el in range(10)}

my_dict = {}
for el in range(10):
    my_dict[el] = str(el)

my_dict = {el: str(el) for el in range(10)}