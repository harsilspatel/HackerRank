laptops = []
for i in range(int(input())):
	name, price = input().split()
	fours = price.count('4')
	sevens = price.count('7')
	if (fours != 0 and sevens != 0) and (fours == sevens):
		laptops.append([int(price), name])
if len(laptops) == 0: print(-1)
else:
	minimum = laptops[0][0]
	minIndex = 0
	for i in range(len(laptops)):
		if laptops[i][0] < minimum: minimum = laptops[i][0]
		minIndex = i
	print(laptops[minIndex][1])