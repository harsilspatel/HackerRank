initialPositionOne, velocityOne, initialPositionTwo, velocityTwo = map(int, input().split())
n = 0

if((initialPositionOne>=initialPositionTwo and velocityOne>=velocityTwo) or (initialPositionOne<=initialPositionTwo and velocityOne<=velocityTwo)):
	print('NO')
else:
	while True:
		theyMeet = False
		n += 1
		
		if(initialPositionOne + (n*velocityOne) == initialPositionTwo + (n*velocityTwo)):
			print('YES')
			theyMeet = True
			break
		if(initialPositionOne + (n*velocityOne) > initialPositionTwo + (n*velocityTwo)):
			break
			
	if(theyMeet == False):
		print('NO')