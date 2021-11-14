binStr = input("Enter a Binary Number/Octal NUmber to convert to Decimal: ")
baseVal = int(input("Enter Base Number: "))
binList = []
index = []
deciSum = 0

for i in binStr:
    binList.append(int(i))
binList.reverse()

for k in range(len(binList)):
    index.append(k)

for j in binList:
    deciSum = deciSum + (j * (baseVal**index[0]))
    index.pop(0)

print("Decimal conversion of ", binStr, " is", deciSum)
