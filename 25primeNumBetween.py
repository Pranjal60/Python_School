n1 = int(input('Enter Number 1:'))
n2 = int(input('Enter Number 2:'))
# Outer Loop
for i in range(n1, n2):
    flag = 0
    if i > 1:
        for j in range(2, int((i/2)+1)):
            if i % j == 0:
                flag = 1
                break
        if flag != 1:
            print(i)
