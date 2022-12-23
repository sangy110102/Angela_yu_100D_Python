#tip calculator
print('Welcome to tip calculator!')
bill = input('What is the total bill? $')
percentageTip = input('What percentage tip would you like to give? 10 or 12 or 15? ')
splitBill = input('How many people to split the bill? ')
billFloat = float(bill)
percentageTipInt = int(percentageTip)/100
splitBillInt = int(splitBill)
pay = (billFloat+billFloat*percentageTipInt)/splitBillInt
payRound = round(pay,2)
message = f'Each person should pay: ${payRound}'
print(message)