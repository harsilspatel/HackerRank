length, operations = list(map(int, input().split()))
array = [0]*(length + 1)
for _ in range(operations):
	start, end, value = list(map(int, input().split()))
	for i in range(start, end+1):
		array[i] += value
		
print(max(array))