n = int(input().strip())
positive, negative, zero = 0.0, 0.0, 0.0
arr = [float(arr_temp) for arr_temp in input().strip().split(' ')]
for i in range(len(arr)):
	if arr[i] > 0: positive+=1
	elif arr[i] == 0: zero+=1
	else: negative+=1
print(float(positive/n), float(negative/n), float(zero/n), sep='\n')