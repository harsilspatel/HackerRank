input()
birds = list(map(int, input().split()))
maxCount = 0
maxBird = 0
for i in set(birds):
	if birds.count(i) > maxCount:
		maxCount = birds.count(i)
		maxBird = i

print(maxBird)