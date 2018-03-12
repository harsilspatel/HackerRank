def fibonacciModified(n):
	if n in fibonacciSequence:
		return fibonacciSequence[n]
	else:
		result = fibonacciModified(n-2) + fibonacciModified(n-1)**2
		fibonacciSequence[n] = result
		return result

t1, t2, n = input().strip().split(' ')
t1, t2, n = [int(t1), int(t2), int(n)]
fibonacciSequence = {0:0, 1:t1, 2:t2}
result = fibonacciModified(n)
print(result)

