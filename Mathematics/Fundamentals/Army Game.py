import math
n, m = input().strip().split()
n, m = int(n), int(m)
print(math.ceil(n/2) * math.ceil(m/2))