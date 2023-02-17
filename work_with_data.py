import datetime

a = datetime.datetime(1997, 1, 17)

print(a.year)
print(a.month)
print(a.day)

b = datetime.date.today().strftime("%d//%m//%Y")
print(b)
print('-------------------------------------')
c = datetime.datetime.now()
print(c)
delta = c - a
print(delta.days)
print(delta.days * 24)
'''
print(delta.microseconds)
print(delta.seconds)

for i in range(5):
    time.sleep(2)
    print('hello')

'''
















