def lcm(x, y):
	if x > y:
		greater = x
	else:
		greater = y
		
	lcm = greater
	
	while (True):
		if (lcm % x == 0 and lcm % y == 0):
			break
		lcm += greater
	return lcm
	
setALength, setBLength = map(int, input().split())
setA = list(map(int, input().split()))
setB = list(map(int, input().split()))

setLCM = 1
for i in range(setALength):
	setLCM = lcm(setLCM, setA[i])
	
countDivisiblity = 0
n = 0
while True:
	n += 1
	isDivisible = True

	for i in range(setBLength):
		if setB[i] % (setLCM*n) != 0:
			isDivisible = False
	
	if isDivisible == True:
		countDivisiblity += 1
	
	if (setLCM*n >= min(setB)):
		break
		
print(countDivisiblity)			
		
			