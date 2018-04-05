row, column = list(map(int, input().split()))
number = 0
if row % 2 == 0:
	number += 1
	row -= 1
number += ((row//2)*10) + ((column-1)*2)
print(number)
