x = int(input("Enter a whole number: "))
n = int(input("Enter a whole number: "))

# power = x**n
# print(x, " raised to the power ", n, " = ", power)
i = 1
while i < n:
    x = x*x
    i += 1
    print(i)
print(x)
