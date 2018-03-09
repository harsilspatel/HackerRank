n = int(input())
array = list(map(int, input().split()))

for i in range(n):
	for j in range(n):
		if i+1 == array[j]:
			print(j+1)
			break