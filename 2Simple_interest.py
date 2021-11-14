principal = float(input("Enter the Principal Amount: "))
rate = float(input("Enter the rate of interest per annum: "))
time = float(input("Enter the time period: "))
ratePercent = (rate/100)*principal

Amount = principal*ratePercent*time
print("The amount at the end will be:",  principal + Amount)
