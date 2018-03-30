N = int(input())
dictionary = dict(input().split() for _ in range(N))

while True:
	query = input()
	
	if query == "":
		break
	
	try:
		value = dictionary[query]
		print("%s=%s"% (query, value))
	except KeyError:
		print("Not found")