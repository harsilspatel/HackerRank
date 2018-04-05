def isPrime(x):
	isPrime = True
	for i in range(2, x):
		if x % i == 0:
			isPrime = False
			break
	return isPrime

for _ in range(int(input())):
	count = 0
	number = int(input())
	for i in range(2, number // 2 + 1):
		if isPrime(i):
			count +=1
#		if number % i == 0:
#			isPrime = True
#			for j in range(2, int(i**1/2) + 1):
#				if i % j == 0:
#					isPrime = False
#					break
#			if isPrime:
#				count += 1
	print(count)