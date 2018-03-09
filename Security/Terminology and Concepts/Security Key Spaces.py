plainText = list(map(int, input().strip("")))
shift = int(input())

for i in range(len(plainText)):
	plainText[i] = (plainText[i]+shift) % 10		
	print(plainText[i], end="")