
from pickle import TRUE


def calculate():

    print("Welcome To The Python Tip Calculator")
        #Prompt the user to enter the amount on the bill
    meal = float(input("What is the total bill?: "))
        #Prompt the user for the % tip they'd like to leave
    tip = int(input("What % tip would you like to give?: "))
        #Prompt the user for the # of people splitting the bill
    people = int(input("How many people are splitting the bill?: "))
          
    
          
        
       
       
     
    

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
    bill_per_person = total_cost / people 
    final_total = round(bill_per_person)
 
     
    #Calculate the amount each person owes based on the bill and tips the user entered
            
    print(f'Your total bill is {final_total} and each person should pay {final_total}')
 
    
    
            
      


 
    
   
   
        
 
    # we need to include an option to continue to calculate for other tip amounts

    another_amount = input('Would you like to enter another amount?')
   
    if another_amount == "n":
        print('I hope you have enjoyed using your Python Tip Calculator!')
        return
    else:
        another_amount == "y"
        return calculate()

        
            
calculate()    