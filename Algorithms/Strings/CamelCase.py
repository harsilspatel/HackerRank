string = input()
words = 1

for i in range(len(string)):
	if string[i].isupper():
		words += 1
	else:
		continue

print(words)