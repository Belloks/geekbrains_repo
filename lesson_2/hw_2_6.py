def inputWithType(inputKey):
    strInput = input("Input product " + inputKey + ": ")
    if inputKey == 'Number':
        return int(strInput)
    elif inputKey == 'Price':
        return float(strInput)
    else:
        return strInput

keys = ['Name', 'Price', 'Number', 'Unit']
continueInput = True
inputList = []
while continueInput:
    newElement = {k: inputWithType(k) for k in keys}
    inputList.append(newElement)
    continueInput = input('Input another one? y/n: ') == 'y'
listOfTuples = []
for ind, element in enumerate(inputList):
    listOfTuples.append((ind + 1, element))
print(listOfTuples)

productAnalyticsMap = {k: list(set([el[k] for ind, el in listOfTuples])) for k in keys}
print(productAnalyticsMap)