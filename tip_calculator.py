
from tkinter.messagebox import YES


def calculate():
    print('Welcome to your Python tip calculator')
#bill amounts are often in decimals so you will need to use the float method
    bill_amount = float(input('Enter the total amount of your bill: $' ))
    
# to find the total amount of your bill including tax you must take your bill amount and multiply it by 10%
    tax = float(bill_amount * 0.10)
    amount = tax + bill_amount
    print(f'Your total bill amount including tax is ${amount}')
   
# now lets find out the tip amount
    tip = float(input('What percentage of your bill would you like to give for a tip? '))
# to find the tip, you will need to have the total bill amount and multiply it by what ever tip amount desired ie 12, 20, 30
#To find the amount fo reach person you will take the total amount plus tip and divide it by the number of guest    
    head_count = int(input('How many people willl spit the bill amount? '))
    each = (amount + (0.01 * tip) * amount / head_count)
    round_each = round(each, 2)
    print(f"Each guest will have to pay ${round_each}")
calculate()
# we need to include an option to continue to calculate for other tip amounts
another_amount = input('Would you like to enter another amount?')
while another_amount == YES:
    calculate()
        
print('I hope you have enjoyed using your Python Tip Calculator!')
    