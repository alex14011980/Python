# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# 2

n = 5


coins = [0, 0, 0, 1, 0, 0, 0]
print(coins.count(0) if coins.count(0) < coins.count(1) else coins.count(1))


# count_zero = 0
# count_one = 0
#
# for coin in coins:
#     if coin == 0:
#         count_zero += 1
#     else:
#         count_one += 1
#
# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)
