my_list = [1, 2, 3, 4, 6, 78, 109, 54, 97]
new_list = list(filter(lambda num: num % 2 == 0, my_list))
print(new_list)



y = lambda a, b: a if a < b else b
print(y(3, 6))


j = list(lambda g = g: g * 10 for g in range(1, 11))
print(type(j))
for h in j:
    print(h())


func('1', 'dfd')
var1 = '1', var2 = 'dfd'
"""
/# filter() and map()


def sum_range(x1, x2):
    sum = 0
    for i in range(x1, x2 + 1, 1):
        sum += i
    return sum


x1 = int(input())
x2 = int(input())
print(sum_range(x1, x2))


corr_pasword = 'qwert12345'


def func(*args):
    string = str(input())
    print(type(args))
    print(type(string))
    print(*args)
    if string == args:
        return True
    else:
        return False


if func(corr_pasword):
    print('Доступ разрешен')
else:
    print('Доступ закрыт')


Необходимо написать функция sum_range(start, end)
"""
