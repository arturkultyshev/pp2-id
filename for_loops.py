string = str(input())
glasno = 'aeyiou'

for i in string:
    if not i in glasno:
        print(i)

for j in range(0, 100):
    print(j)