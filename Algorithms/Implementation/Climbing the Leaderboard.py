def climbingLeaderboard(scores, alice):
	length = len(scores)
	scoreSet = sorted(set(scores))
	result = []
#	print(alice)
	
	for aliceScore in alice:
		for rank, score in enumerate(scoreSet):
			if aliceScore < score:
				result.append(length - rank - 1)
				break
	if len(result) != len(scoreSet):
		result.append(1)
	return result
		
	

n = int(input().strip())
scores = list(map(int, input().strip().split(' ')))
m = int(input().strip())
alice = list(map(int, input().strip().split(' ')))
result = climbingLeaderboard(scores, alice)
print ("\n".join(map(str, result)))