#number = 100
#if number == 100):
#	print('Its a 5')
#	print('bleh')
#	bird = 1000
#else:
#	print('Not a five')
#	print('booooo')
#	bird = 150
#

#score = 7
#
#if score > 80:
#	print('HD')
#elif score > 70:
#	print('D')
#elif score > 60:
#	print('C')
#elif score > 50:
#	print('P')
#else:
#	print('Gond marai Madarchod')

#
#rollNumber = [70, 76, 8, 4, 54, 100]
#for i in rollNumber:	
#	if i > 80:
#		grade = 'HD'
#	elif i > 70:
#		grade = 'D'
#	elif i > 60:
#		grade = 'C'
#	elif i > 50:
#		grade = 'P'
#	else:
#		grade = 'F'
#		
#	print(i, grade)

number = 1000000
factors = 2
for i in range(2, number):
	if number % i == 0:
		factors += 1
		print(i)

if factors > 2:
	print('Its a composite #')
else:
	print('Prime #')








