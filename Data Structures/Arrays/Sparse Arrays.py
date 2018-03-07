#import collections
#
#values = collections.defaultdict(int)
#for _ in range(int(input())):
#	values[input()] += 1
#for _ in range(int(input())):
#	print(values[input()])

strings = []
for _ in range(int(input())):
	strings.append(input())
for _ in range(int(input())):
	print(strings.count(input()))