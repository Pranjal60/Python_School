# Using the while loop
num = int(input("Enter a num to find the factors"))
print(1, end=" ")
count = 2
while count <= num/2:
    if num % count == 0:
        print(count, end=" ")
    count += 1
print(num, end=" ")

print('\n')
print('\n')
# Using the for loop
num = int(input("Enter a number to find the factors"))
print(1, end=" ")
c = int(num/2)
for i in range(2, c+1):
    if num % i == 0:
        print(i, end=" ")
print(num, end=" ")
