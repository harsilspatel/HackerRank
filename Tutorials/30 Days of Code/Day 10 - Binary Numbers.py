decimalNumber = int(input())
binaryNumber = ""

while True:
	binaryNumber += str(decimalNumber%2)
	decimalNumber = int(decimalNumber/2)
	if decimalNumber == 0:
		binaryNumber = binaryNumber[::-1]
		break
temp = 1
consecutiveOnes = 1
i = 1
for i in range(len(binaryNumber)-1):
	if binaryNumber[i] == "1" and binaryNumber[i + 1] == "1":
		temp += 1
	else:
		temp = 1
	
	if temp > consecutiveOnes:
		consecutiveOnes = temp
		
print(consecutiveOnes)