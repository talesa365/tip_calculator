
print("Welcome To The Python Tip Calculator")
#Create a function to calculate the split costs of the customers bill
def calculate():    
    #Prompt the user to enter the amount on the bill
    meal = float(int(input("What is the total bill?: ")))
    #Prompt the user for the % tip they'd like to leave
    tip = int(input("What % tip would you like to give?: "))
    #Prompt the user for the # of people splitting the bill
    people = int(input("How many people are splitting the bill?: "))

   #tax amount was given in the instructions
    tax = .10
    print(tax)
    #figure the tip on the bill amount pre tax 
    tip_amount = meal * tip/100
    print(f'Your meal was ${meal} and your tip is ${tip_amount}')
    #figure the sales tax from the bill amount    
    tax_amount = meal * tax
    #calculate the total bill to include tax and tip
    total_cost = tip_amount + tax_amount + meal
    #update the bill to include the tax   
    print(f' Your total with tax is ${total_cost}')
     #Calculate the amount each person owes based on the bill and tips the user entered     
    bill_per_person = total_cost / people 
    final_total = bill_per_person
    print(f'Your total bill is {total_cost} and each person should pay {final_total}')
calculate()
 
    # we need to include an option to continue to calculate for other tip amounts
def ask_again():
    another_amount = input('Would you like to enter another amount? ')
    print(another_amount)
    for letter in another_amount:
        if letter == "n":
            print('I hope you have enjoyed using your Python Tip Calculator!')
            return
        else:
            another_amount == "y"
            result = calculate()
            return result

      
ask_again()   
