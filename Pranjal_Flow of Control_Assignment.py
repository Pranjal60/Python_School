# Program to calculate the area and perimete of a circle and a rectange
print("Choose Circle or rectangle")
operation = input("Enter: ")

# Flow of control
# if
if(operation.lower() == "circle"):
    print("To calculate the area write Area, and to calculate the perimeter write Preimeter")
    Calc = input("Enter:")
    rad = float(input("Enter Radius: "))
    pi = 3.14
    if(Calc.lower() == "area"):
        print("The area of the circle with radius ", rad, "is", pi*rad*rad)
    else:
        print("The Perimeter of the circle with radius ", rad, "is", 2*pi*rad)

# Elif
elif(operation.lower() == "rectangle"):
    print("To calculate the area write Area, and to calculate the perimeter write Preimeter")
    Calc = input("Enter:")
    length = float(input("Enter the length: "))
    width = float(input("Enter the Width: "))
    if(Calc.lower() == "area"):
        print("The area of the rectangle = ", length*width)
    else:
        print("The Perimeter of the rectangle = ", 2*(length+width))

# else
else:
    print("Invalid input")
