n, k = map(int, input().split())
array = list(map(int, input().split()))
divisibleNumbers = 0

for i in range(len(array)):
	for j in range(i+1, len(array)):
		if ((array[i] + array[j])%k == 0):
			divisibleNumbers = divisibleNumbers + 1

print(divisibleNumbers)