# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

# n = input('Введите номер билета ')

n = int(input('Введите размер стороны n:  '))
m = int(input('Введите размер стороы m: '))
k = int(input('Сколько долек отломить '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')