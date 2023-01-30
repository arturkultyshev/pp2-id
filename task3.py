"""
56789 = 5, 6, 7, 8, 9
Even: ---
Odd: ---
"""

num = input()

even = 0
odd = 0

for i in num:
    if int(i) % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print(even, odd)
