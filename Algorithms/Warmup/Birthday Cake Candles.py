n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]
countCandles = 1

height.sort(reverse = True)

for i in range(len(height)-1):
	if height[i] == height[i+1]: countCandles+=1
	else: break

print(countCandles)