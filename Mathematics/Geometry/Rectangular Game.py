rows = []
columns = []
for _ in range(int(input())):
	row, column = list(map(int, input().split()))
	rows.append(row)
	columns.append(column)
print(min(rows)*min(columns))