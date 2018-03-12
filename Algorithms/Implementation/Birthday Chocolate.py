#chocolateLength = int(input())
#chocolateBar = list(map(int, input().split()))
#theSum, subsetLength = map(int, input().split())
#calculatedSum, ways = 0, 0
#
#for i in range(chocolateLength - subsetLength):
#	calculatedSum = 0
#	for j in range(subsetLength):
#		calculatedSum += chocolateBar[i+j]
#	if(theSum == calculatedSum):
#		ways += 1
#
#if subsetLength == 1:
#	if chocolateBar[0] == sum:
#		ways = 1
#		
#print(ways)

input()
chocolates = list(map(int, input().split()))
day, month = list(map(int, input().split()))
ways = 0

for i in range(len(chocolates) - month + 1):
	theSum =  0
	for j in range(month):
		theSum += chocolates[i+j]
#	print(theSum)
	if theSum == day: ways += 1

print(ways)
