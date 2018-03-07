strings = []
badStrings = []
goodSet = True
for _ in range(int(input())):
	string = input()
	for i in strings:
		if i in string:
			goodSet = False
			badStrings.append(string)
	strings.append(string)
print('GOOD SET') if goodSet else print('BAD SET')
if not goodSet: print(badStrings[0]) 