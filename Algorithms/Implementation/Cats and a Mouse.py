testcase = int(input())

for _ in range(testcase):
	a, b, c = map(int, input().split())
	if abs(a-c) == abs(b-c):
		print("Mouse C")
	elif abs(a-c) > abs(b-c):
		print("Cat B")
	else:
		print("Cat A")