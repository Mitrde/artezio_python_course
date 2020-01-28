inputList = ['abc', 'xyz', 'aba', '1221', "1"]
count = 0
for word in inputList:
    if len(word) > 1 and word[0] == word[-1]:
        count += 1
print(count)
