n = int(input())
array = list(map(int, input().split()))

for i in range(n):
	print(array[array[i]-1])