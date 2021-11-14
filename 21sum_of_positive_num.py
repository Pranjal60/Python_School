# Using While loop
sum = 0
while True:
    num = int(input("Enter +ve int only -ve int would break the loop"))
    if num < 0:  # using if condition to check num type instead of else
        break
    sum += num
print(sum)
