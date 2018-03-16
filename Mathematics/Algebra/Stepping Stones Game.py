for _ in range(int(input())):
	targetBlock = int(input())
	
	for i in range(1, targetBlock):
		block = i*(i+1)/2
		if block == targetBlock:
			print('Go On Bob', i)
			break
		if block > targetBlock:
			print('Better Luck Next Time')
			break
		