n = int(input().strip())
for i in range(n):
	for _ in range(0, n-1-i):
		print(' ', end='')
	for _ in range(0, i+1):
		print('#', end='')
	print('')