'''
Задача №35.Напишите функцию, которая принимает одно число и проверяет,
является ли оно простым Напоминание: Простое число - это число,
которое имеет 2 делителя: 1  и n(само число)
Input: 5
Output: yes
'''


# def natural_number(n):
#     d = 2
#     while d * d <= n and n % d != 0:
#         d += 1
#     return d * d > n
#
#
# n = int(input())
# if natural_number(n):
#     print('YES')
# else:
#     print('NO')


def func_1(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
    return flag

print(func_1(10))

def func_2(num, flag=True, i = 2):
    if i < num:
        if num % i == 0:
            flag = False
            return func_2(num, flag, i + 1)
    return flag
print(func_2(31))