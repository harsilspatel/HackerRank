time = input().strip()
hour = int(time[0:2])
meridiem = time[8:10]
if (hour == 12) and (meridiem == 'AM'): print('00'+time[2:8])
elif (hour < 12) and (meridiem == 'PM'):
	hour+=12
	print(str(hour)+time[2:8])
else: print(time[0:8])