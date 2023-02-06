# : Найдите сумму цифр трехзначного числа. 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number = int(input('Введите трехзначное число '));
# sum =0
# ed = number%10
# de = number//10%10
# sot = number//100
# sum = ed+de+sot

# print(f'{sum}')

number = (input('Введите трехзначное число '))
a = int(number[0])
b = int(number[1])
c = int(number[2])
print(a+b+c)