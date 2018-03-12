array = list(map(int, input().split()))
array.sort()
sum = sum(array)
print(sum-array[-1], sum-array[0], sep=' ')