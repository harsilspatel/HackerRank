n = int(input())
array = list(map(int, input().split()))

array.sort()
mean = sum(array)/n

if n % 2 == 0:
	median = (array[(n//2)-1] + array[n//2])/2
else:
	median = array[(n-1)//2]

frequecy = {}
mode = [array[0], 0]
for i in array:
	if i not in frequecy.keys():
		frequecy[i] = 1
	else:
		frequecy[i] += 1
	
	if frequecy[i] > mode[1]:
		mode[0] = i
		mode[1] = frequecy[i]
		
print("%.1f\n%.1f\n%d" % (mean, median, mode[0]))
	