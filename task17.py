# Задача №17. Дан список чисел. Определите, сколько
# в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

num_list = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(num_list)))

# традиционный итератор с функцией append()
lst = []
for el in num_list:
    if el not in lst:
        lst.append(el)
print(len(lst))



