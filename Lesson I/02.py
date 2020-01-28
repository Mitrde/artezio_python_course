S = input()

letterDict = dict()

for letter in S:
    letterDict[letter] = 0
for letter in S:
    letterDict[letter] += 1

print(letterDict)

