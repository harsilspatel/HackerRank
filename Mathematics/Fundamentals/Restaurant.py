import fractions

for _ in range(int(input())):
	length, breadth = list(map(int, input().split()))
	gcd = fractions.gcd(length, breadth)
	print(length*breadth//(gcd**2))
