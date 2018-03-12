n = int(input())
colorArray = list(map(int, input().split()))

colorDict = {}

for i in range(n):
	if colorArray[i] in colorDict:
		colorDict[colorArray[i]] += 1
	else:
		colorDict[colorArray[i]] = 1
		
sockPairs = 0

for i in colorDict.values():
	sockPairs += int(i/2)

print(sockPairs)