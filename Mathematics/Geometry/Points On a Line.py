x = []
y = []
for i in range(int(input())):
	a, b = map(int, input().split())
	x.append(a)
	y.append(b)
x.sort()
y.sort()
if (x[-1] == x[0] or y[-1] == y[0]):
	print ("YES")
else:
	print ("NO")