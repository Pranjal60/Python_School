num = int(input("Enter the number till which u want the pattern"))
for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
