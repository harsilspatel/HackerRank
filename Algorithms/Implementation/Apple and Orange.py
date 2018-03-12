houseStart, houseEnd = map(int, input().split())
appleTree, orangeTree = map(int, input().split())
apples, oranges = map(int, input().split())
appleDistance = list(map(int, input().split()))
orangeDistance = list(map(int, input().split()))
applesOnHouse = 0
orangesOnHouse = 0

for i in range(apples):
	if((appleTree + appleDistance[i] >= houseStart) and (appleTree + appleDistance[i] <= houseEnd)):
		applesOnHouse += 1
print(applesOnHouse)

for i in range(oranges):
	if((orangeTree + orangeDistance[i] >=  houseStart) and (orangeTree + orangeDistance[i] <= houseEnd)):
		orangesOnHouse += 1
print(orangesOnHouse)