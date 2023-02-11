# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите число: "))
a = 2  
my_list = []
while a <= number:
    if number % a == 0:
        my_list.append(a)
        number //= a
        a = 2
    else:
        a += 1
print('Простые множители числа:', my_list)