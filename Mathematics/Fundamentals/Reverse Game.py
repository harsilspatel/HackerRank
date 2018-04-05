for _ in range(int(input())):
	n, k = list(map(int, input().split()))
#	balls = list(range(n))[::-1]
#	for i in range(1, n - 1):
#		balls = balls[:i] + balls[i:][::-1]
#		print(balls)
#	print(balls.index(k))
	
	balls = list(range(n))
	finalBalls = []
	for i in range(n//2 + 1):
		finalBalls.append(balls[-i-1])
		finalBalls.append(balls[i])
	
	print(finalBalls.index(k))