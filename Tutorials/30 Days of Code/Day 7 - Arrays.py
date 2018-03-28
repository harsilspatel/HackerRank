N = int(input())
array = list(input().split())
array.reverse()
for i in range(N):
	print(array[i], sep="", end=" ")