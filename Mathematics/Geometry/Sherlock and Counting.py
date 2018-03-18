for _ in range(int(input())):
	n, k = map(int, input().split())
	count = 0
	for i in range(1, n):
		if i*(n-i) <= n*k: count += 1
	print(count)