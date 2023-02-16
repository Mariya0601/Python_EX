# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input("введите число а"))
b = int(input("введите число b"))
def step_num(a,b):
    if b==0:
        return 1
    return a*step_num(a, b-1)
res = step_num(a,b)
print(res)