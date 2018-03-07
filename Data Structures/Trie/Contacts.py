#contacts = []
#for _ in range(int(input())):
#	action, string = input().split()
#	if action == 'add': contacts.append(string)
#	else: print(sum([1 for i in range(len(contacts)) if string in contacts[i]]))

import collections
contacts = collections.defaultdict(int)
for _ in range(int(input())):
	action, string = input().split()
	if action == 'add':
		for i in range(len(string)):
			contacts[string[:i+1]] += 1
	else: print(contacts[string])