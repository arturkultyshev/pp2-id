def func(*args):
    for index, item in enumerate(*args):
        print(f'var{index + 1} = {item}')



func([2, 4, 'asd', 7, [3, 4, 5], 9])

"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = start b = end 

"""