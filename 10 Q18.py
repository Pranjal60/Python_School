num = int(input("Enter a number: "))
sum = 0
for i in range(0, num + 1):
    if i % 2 != 0:
        sum = sum + i
print(sum, "is the sum of all the ODD numbers from 0 to", num)
