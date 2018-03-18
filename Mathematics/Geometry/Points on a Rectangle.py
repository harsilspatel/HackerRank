for _ in range(int(input())):
	x = []
	y = []
	Rectangle = True
	for _ in range(int(input())):
		a, b = list(map(float, input().split()))
		if (len(x) != 2) and (a not in x): x.append(a)
		if (len(y) != 2) and (b not in y): y.append(b)
		if (a in x) or (b in y): continue
		else: Rectangle = False
	if Rectangle: print('YES')
	else: print('NO')

#	for _ in range(int(input())):
#		a, b = list(map(float, input().split()))
#		x.append(a)
#		y.append(b)
#	if (len(set(x)) <= 2) and (len(set(y)) <= 2): print('YES')
#	else: print('NO')