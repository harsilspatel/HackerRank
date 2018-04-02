import functools
for _ in range(int(input())):
	input()
#	paths = list(map(int, input().split()))
#	product = 1
#	for path in paths: product *= path
#	print(product % 1234567)
	print(functools.reduce(lambda x,y:x*y, list(map(int, input().split()))) % 1234567)