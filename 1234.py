my_list = [1,2,3,4,5,6,7,8,9,10]
start = int(input())
end = int(input())
new_list = list(filter(lambda x : start <= x < end +1, my_list))
print(new_list)