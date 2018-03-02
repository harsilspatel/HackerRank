a = 0b10
b = 0b1010
theSum = 0
for i in range(314159+1):
	theSum += (a ^ (b << i)) 

print(theSum % (10**9 + 7))
