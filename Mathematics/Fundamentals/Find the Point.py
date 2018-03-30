for _ in range(int(input())):
	points = list(map(int, input().split()))
	print((2*points[2] - points[0]), (2*points[3] - points[1]))