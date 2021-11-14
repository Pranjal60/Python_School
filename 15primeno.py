n = int(input('Enter a number: '))
for i in range(1, 100):
    n = n % i
    print(n)
    # if(n%i==0):
    #     pass
