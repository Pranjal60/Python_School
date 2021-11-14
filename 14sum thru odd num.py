# 0, 3, 8, 15, 24 . . . n
n = int(input('Enter n: '))
s = 1
for i in range(1, n+1):
    s = (i**2)-1
    print(s)
    # print(i)
