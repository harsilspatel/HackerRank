games = int(input())
gameScores = list(map(int, input().split()))

greatest, least = gameScores[0], gameScores[0]
countGreatest, countLeast = 0, 0

for i in range(games):
	if(gameScores[i] > greatest):
		greatest = gameScores[i]
		countGreatest += 1
	elif(gameScores[i] < least):
		least = gameScores[i]
		countLeast += 1

print(countGreatest, countLeast)