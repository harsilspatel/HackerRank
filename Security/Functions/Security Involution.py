n = int(input())
array = list(map(int, input().split()))
isInvolution = True

for i in range(n):
	if i+1 != array[array[i]-1]:
		isInvolution = False

if isInvolution:
	print("YES")
else:
	print("NO")