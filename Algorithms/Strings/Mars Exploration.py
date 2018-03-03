S = input()
sos = "SOS"
count = 0

for i in range(len(S)):
	if S[i] != sos[i % 3]: count += 1
	
print(count)