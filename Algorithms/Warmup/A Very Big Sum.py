sum = 0
n = input() #Not needed for the code, Python is smart <3
array = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for i in array:
	sum += i
print(sum)