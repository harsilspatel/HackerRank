testcase = int(input())

for _ in range(testcase):
	string = input()

	for i in range(0, len(string), 2):
		print(string[i], end="")
	print(" ", end="")
	for i in range(1, len(string), 2):
		print(string[i], end="")
	print("")