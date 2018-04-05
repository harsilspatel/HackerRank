import sys

def addHourGlass(x, y):
	sum = array2D[x-1][y-1] + array2D[x-1][y] + array2D[x-1][y+1]
	sum += array2D[x][y]
	sum += array2D[x+1][y-1] + array2D[x+1][y] + array2D[x+1][y+1]
	return (sum)
	
array2D = []
for _ in range(6):
	array1D = list(map(int, input().split()))
	array2D.append(array1D)

maxSum = - sys.maxsize
for i in range(1, 5):
	for j in range(1, 5):
		sum = addHourGlass(i, j)
		if sum > maxSum:
			maxSum = sum

print(maxSum)