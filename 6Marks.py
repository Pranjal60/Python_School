list = []
for i in range(6):
    list.append(float(input('Enter Your Marks: ')))

# Sum
add = sum(list)

# Average
Av = add/6

# Grade
Grade = ""
if(add >= 550):
    Grade = "A"
elif(add >= 400):
    Grade = "B"
elif(add >= 350):
    Grade = "C"
elif(add >= 200):
    Grade = "D"
else:
    Grade = "E"

# Final Print
print("Write A for Total. Write B for Average. Write C for Grade")
menu = input("Enter your choice:")
if(menu == "A"):
    print('Your Total = ', add)
elif(menu == "B"):
    print('Your Average = ', Av)
else:
    print('Your Grade = ', Grade)
    if(Grade == "A"):
        print("Congratualtions You Are Amazing!!!")
    elif(Grade == "B"):
        print("Ohh You got a B, Not Bad")
    elif(Grade == "C"):
        print("Good Attempt! I know next time you'll score grate!")
    else:
        print("You did an amazing attempt, you will surely get good next time .... and remember... You are Amazing!!!")