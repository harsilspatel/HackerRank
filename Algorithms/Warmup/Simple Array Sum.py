sum = 0
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for i in arr:
	sum += i
print(sum)