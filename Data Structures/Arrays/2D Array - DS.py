array = []
for _ in range(6):
	array.append([int(i) for i in input().strip().split(' ')])

theSums = []
for column in range(1, 5):
	for row in range(1, 5):
		theSums.append((sum(array[row-1][column-1:column+2]) + sum(array[row+1][column-1:column+2]) + array[row][column])
print(max(theSums))