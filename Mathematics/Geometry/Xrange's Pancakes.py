sides, cooks = list(map(int, input().split()))
rotationsAdjust = 0
rotations = []
flips = []
flipAdjust = 0
for _ in range(cooks):
	action, axis = list(map(int, input().split()))
	if action == 1:
		rotations.append(axis)
		rotationsAdjust = (rotationsAdjust + axis) % sides 
	if action == 2:
		flips.append(axis)
#		print(flipAdjust)
#		flipAdjust = -flipAdjust
print(sum(rotations)% sides )
oddSum = 0
evenSum = 0
for i in range(0, len(flips), 2): evenSum += flips[i]
for i in range(1, len(flips), 2): oddSum += flips[i]
#print(evenSum - oddSum)
	
if len(flips) % 2 == 0: print(1, sides - rotationsAdjust)
else: print(2, (evenSum - oddSum))