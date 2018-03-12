totalPages = int(input())
targetPage = int(input())

frontStart = targetPage//2
if totalPages % 2 == 1: backStart = (totalPages - targetPage) // 2
else: backStart = (totalPages - targetPage + 1) // 2
print(min(frontStart, backStart))