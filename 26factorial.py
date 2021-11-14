num = int(input("Enter the number to get it's Factorial"))
if num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(num-1, 0, -1):
        num *= i
    print(num)
