# """
#
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
#
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
#
# Пример:
# n = 385916 -> yes
# n = 123456 -> no
# """

n = 385916
n = int(n)
sum_left = 0
sum_right = 0
for i in range(6):
    if i<3:
        sum_right += n // 10**i % 10
    else:
        sum_left  += n // 10**i % 10
if sum_left == sum_right:
    print('yes')
else:
    print('no')