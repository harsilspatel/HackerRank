n, k = map(int, input().split())
priceArray = list(map(int, input().split()))
amountCharged = int(input())

totalAmount = 0

for i in range(n):
	totalAmount += priceArray[i]
	
amountActual = (totalAmount - priceArray[k])/2

if amountActual == amountCharged:
	print("Bon Appetit")
else:
	print(int(amountCharged - amountActual))