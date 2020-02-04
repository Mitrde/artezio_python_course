S = input()
nameList = S.split()

for i in range(len(nameList)):
    nameList[i] = nameList[i].capitalize()

S = ' '.join(nameList)

print(S)
