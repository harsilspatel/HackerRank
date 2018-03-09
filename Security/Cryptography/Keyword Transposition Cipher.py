testcase = int(input())

for _ in range(testcase):
    keyword = list(input().strip(""))
    cipherText = input()

    keywordSet = []
    for i in range(len(keyword)):
        isDuplicate = False
        for j in range(len(keywordSet)):
            if keyword[i] == keywordSet[j]:
                isDuplicate = True
                break
        if isDuplicate == False:
            keywordSet.append(keyword[i])
            
    # To create a ABCD...Z
    columns = len(keywordSet)
    for i in range(65, 91):
        isDuplicate = False
        for j in range(columns):
            if ord(keywordSet[j]) == i:
                isDuplicate = True
                break
        if isDuplicate == False:
            keywordSet.append(chr(i))

    # To sort ABC...Z in alphabetical order of the keyword
    sortedKeywordSet = sorted(set(keyword))
    substitution = {}
    for i in range(columns):
        for j in range(columns):
            if sortedKeywordSet[i] == keywordSet[j]:
                for n in range(j, 26, columns):
                    substitution[keywordSet[n]] = len(substitution)
                break

    # To print the values
    for i in range(len(cipherText)):
        if cipherText[i] == " ":
            print(" ", end="")
        else:
            print(chr(substitution[cipherText[i]] + 65), end="")
    
    print("")