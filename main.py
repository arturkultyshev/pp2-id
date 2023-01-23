a = int(input('Input 1 num'))
b = int(input("Input 2 num"))
znak = str(input('Input znak'))

if znak == '+':
    print(a + b)
elif znak == '-':
    print(a - b)
elif znak == '/':
    if b != 0:
        print(a / b)
    else:
        print("На ноль делить нельзя")
elif znak == '*':
    print(a * b)
else:
    print('Я не знаю такого знака')





"""
!= не равно
== равенство
"""