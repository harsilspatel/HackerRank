for _ in range(int(input())):
	string = input()
	hackerRank = "hackerrank"
	charIndex = 0
	isPresent = False
	i, j = -1, -1

	while True:
		i += 1
		isPresent = False
		while True:
			j += 1
			if j == len(string): break
			if hackerRank[i] == string[j]:
				isPresent = True
				break
			if j == len(string): break
			
		if isPresent == False:
			print("NO")
			break
			
		if isPresent and i == 9:
			print("YES")
			break
			
		if i == len(hackerRank): break
