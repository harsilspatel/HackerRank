alice = tuple(map(int, input().split())) #alice = [int(n) for n in input().split()]
bob = tuple(map(int, input().split()))
alicePoints = 0
bobPoints = 0

for i in range(len(alice)):
	if alice[i] > bob[i]: alicePoints+=1
	if bob[i] > alice[i]: bobPoints+=1
	
print(alicePoints, bobPoints)