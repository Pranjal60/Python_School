end = int(input("Enter the number till which you want the sum: "))
sum = 0
for i in range(1, end+1):
    print(i)
    sum = sum+i
print("The sum of all the numbers above is: ", sum)
