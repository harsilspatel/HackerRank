n = int(input())
array = list(map(int, input().split()))

if ((n == len(array)) and (len(array) == len(set(array)))):
	print("YES")
else:
	print("NO")