'''
Задача №33. Хакер Василий получил доступ к классному журналу
и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия,
но наоборот: все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''
# lst = [1, 3, 3, 3, 4]
# mi = min(lst)
# ma = max(lst)
# lst_1 = [mi if i == ma else i for i in lst]
# print(lst_1)

def min_to_max(grade_list, count, x):
    if count < 0:
        return grade_list
    count -= 1
    if grade_list[count] == x:
        grade_list[count] = min(grade_list)
    return min_to_max(grade_list, count, x)


list_1 = [1, 3, 3, 3, 4]
cnt = 5

print(min_to_max(list_1, cnt, max(list_1)))