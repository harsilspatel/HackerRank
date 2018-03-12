testcase = int(input())
grade = 0
for _ in range(testcase):
	grade = int(input().strip())
	if(grade<38):
		print(grade)
	elif(grade%5==3 or grade%5==4):
		print(grade+5-(grade%5))
	else:
		print(grade)