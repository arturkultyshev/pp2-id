import work_with_data

"""
ax^2 + bx + c = 0

0.6x^2 + 8x - 10 = 0
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

diskr = b ** 2 - 4 * a * c

if diskr > 0:
    x1 = (-b + math.sqrt(diskr)) / (2 * a)
    x2 = (-b - math.sqrt(diskr)) / (2 * a)
    print(f'x1 = {x1} \n x2 = {x2}')
elif diskr == 0:
    x = -b / (2 * a)
    print(f'x1 = x2 = {x}')
else:
    print('No x')
