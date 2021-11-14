def totalPayable():
    no = int(input("Enter the number of items you bought: "))
    list = []
    total = 0

    # Total price calculation
    for i in range(1, no+1):
        price = float(input("Enter the price: "))
        quantity = int(input("Enter the quantity: "))
        tb = price*quantity
        list.append(tb)
    for t in range(0, len(list)):
        total = total + list[t]
    print("Your total bill is ", total)

    # Shop Member???
    sm = input("Are you a shop member???  Yes or No")
    if sm.lower() == 'yes':
        print("You'll get an additional discount of 5%")
        total = total - (5/100)*total
    else:
        print("You need to be a member of the shop in order to avail an additional discount of 5%")

        # flow of control
    if total >= 500 and total < 1000:
        discountTotal = total - ((5/100)*total)
        print("you get a discount of 5%", " and your total is ", discountTotal)

    elif total >= 1000 and total < 2000:
        discountTotal = total - ((8/100)*total)
        print("you get a discount of 8%", " and your total is ", discountTotal)

    elif total >= 2000:
        discountTotal = total - ((10/100)*total)
        print("you get a discount of 10%", " and your total is ", discountTotal)

    else:
        print("Your total Bill is ", total)


totalPayable()
