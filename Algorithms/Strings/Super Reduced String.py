string = input()
i = 0

while True:
	resetI = False
	if string[i] == string[i+1]:
		string = string.replace(str(string[i]+string[i+1]), "")
		resetI = True
	
	if resetI == False:
		i += 1
	else:
		i = 0
	
	if string == "":
		print("Empty String")
	
	if i == (len(string)-1):
		break

if string != "":
	print(string)