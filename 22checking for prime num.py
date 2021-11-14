# For loop
num = int(input("Enter a number to check whether it's Prime or not "))
flag = 0
if num > 1:
    for i in range(2, int(num/2)):
        if num % i == 0:
            flag = 1
            break

    if flag == 1:
        print("NOT prime")
    else:
        print("PRIME")

print('\n')
print('\n')

# While loop
num = int(input("Enter a number to check whether it's Prime or not "))
f = 2
if num > 1:
    while f <= int(num/2):
        if num % f == 0:
            print("NOT prime")
            break
        f += 1
    else:
        print("PRIME")
