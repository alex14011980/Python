'''
Задача №37. Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять
массивы и использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 32

'''

def rev(n):
    if n > 0:
        num = int(input("Введите число: "))
        rev(n - 1)
        print(num, end=' ')
rev(2)