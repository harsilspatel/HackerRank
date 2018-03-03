n = int(input())
array = input()
shift = int(input())
shift = shift % 26

for i in array:
	if 64 < ord(i) and ord(i) < 91:
		if ord(i) + shift > 90:
			i = chr(ord(i) + shift - 26)
		else:
			i = chr(ord(i) + shift)		
	elif 96 < ord(i) and ord(i) < 123:
		if ord(i) + shift > 122:
			i = chr(ord(i) + shift - 26)
		else:
			i = chr(ord(i) + shift)
			
	print(i, end="")