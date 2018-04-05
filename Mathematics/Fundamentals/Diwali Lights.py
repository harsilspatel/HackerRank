for _ in range(int(input())):
	bulbs = int(input())
	quarter = bulbs // 4
	quarterModulo = 2**quarter % 100000
	partialNumber = (quarterModulo*quarterModulo) % 100000
	anotherPartial = (quarterModulo*(2**(bulbs-3*quarter) % 100000)) % 10000
	theNumber = (partialNumber % 100000)*(anotherPartial % 100000) % 100000
	print(theNumber - 1)