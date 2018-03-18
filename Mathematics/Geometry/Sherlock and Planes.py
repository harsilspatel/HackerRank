# Easy, Copied from discussions.
for _ in range(int(input())):
	x = []
	y = []
	z = []
	for _ in range(4):
		a,b,c = input().split()
		x.append(int(a))
		y.append(int(b))
		z.append(int(c))
	x.sort()
	y.sort()
	z.sort()
	print (["NO", "YES"] [x[3]-x[0]==0 or y[3]-y[0]==0 or z[3]-z[0]==0])