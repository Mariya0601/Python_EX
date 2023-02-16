# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

from random import randint
a = int(input("Введите первый массив:"))
b = int(input("Введите второй массив:"))
array_first = [randint(0,6) for i in range(1,a)]
array_second = [randint(0,6) for i in range(1,b)]

print(array_first)
print(array_second)

i = set(array_first).intersection(set(array_second))
print(sorted(i))