# Programme to calculate compound interest with monthly contribution at end of month

# First calculate the compound interest for principal using formula: A = P (1 + r/n)**(nt)
# r = annual interest rate
# n = number of compounds per period (usually in months)
# t = time

import os

lumpsum = input("Enter your current pension value: ")
annualreturnin = input("Enter your expected annual rate of return: ")
periodin = input("Enter number of times that the interest is compounded per year: ")
yearsin = input("Enter expected time to retirement in years: ")
contributionin = input("Enter monthly contribution amount: ")

# Convert entered input from strings into integers
current = float(lumpsum)
annualrate = (float(annualreturnin))/100
period = int(periodin)
years = int(yearsin)
contributions = float(contributionin)

print ("Your current pension value entered is: ", current)
print ("Your annual expected rate of return in decimal form is: ", annualrate)
print ("The number of times interest is expected to be paid per year is: ", period)
print ("The number of years it will grow: ", years)
print ("Your monthly contribution is: ", contributions)

# calculate compound interest plus the principal
interestperiod = (1 + (annualrate/period))
topower = (period * years)

interestplusprincipal = current * (interestperiod**topower)

#print("The compound interest plus the principal is: ", interestplusprincipal)

# Now calculate the future value with deposits made at the end of the period
# Using formula: Monthly Payment × ( ( ( (1 + r/n)^(nt) ) - 1 ) / (r/n) )
# r = annual interest rate
# n = number of compounds per period (usually in months)
# t = time the money is invested (usually in years)

oneplus = (1+(annualrate/period))
topower2 = ((period*years))
periodrate = annualrate/period

halfdone = (((oneplus**topower2)-1)/periodrate)
futurevaluewithdeposits = contributions*halfdone
#print ("Future value with deposits: ",futurevaluewithdeposits)

totalamount = interestplusprincipal + futurevaluewithdeposits

lump = f"{current:,.2f}"
cont = f"{contributions:,.2f}"
total = float(totalamount)
total2 = f"{total:,.2f}"

os.system('clear')

print ("Expected pension amount given a lump sum of £"+lump + " with monthly contributions of £"+cont + " over " + yearsin + " years at " + annualreturnin+"% return: £"+str(total2))
