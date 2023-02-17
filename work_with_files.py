

with open('test2.txt', 'w') as file:
    for i in range(10):
        file.write(str(i) + '\n')


a = 'abcdef'
with open('test2.txt', 'w') as file:
    for i in a:
        file.write(str(i) + '\n')
