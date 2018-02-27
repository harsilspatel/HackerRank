n = int(input().strip())
a = []
primaryDiagonal = 0
secondaryDiagonal = 0
for a_i in range(n):
	a_t = list(map(int, input().strip()))
	a.append(a_t)
for i in range(n):
	primaryDiagonal += a[i][i]
	secondaryDiagonal += a[i][n-1-i]

print(abs(primaryDiagonal-secondaryDiagonal))