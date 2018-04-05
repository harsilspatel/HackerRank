import math
length, speedOne, speedTwo = list(map(int, input().split()))
rootTwo = math.sqrt(2)
for _ in range(int(input())):
	area = int(input())
	time = rootTwo*(length - math.sqrt(area))/abs(speedOne-speedTwo)
	print(time)