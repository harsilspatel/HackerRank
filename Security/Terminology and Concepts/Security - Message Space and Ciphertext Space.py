plainText = list(map(int, input().strip("")))

for i in range(len(plainText)):
	if plainText[i] < 9:
		plainText[i] += 1
	else:
		plainText[i] = 0
		
	print(plainText[i], end="")