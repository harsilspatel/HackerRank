length, rotations = list(map(int, input().split()))
array = list(map(int, input().split()))
for i in array[rotations%length:] + array[:rotations%length]: print(i, end = ' ')