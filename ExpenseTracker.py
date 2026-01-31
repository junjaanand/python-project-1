# expense tracker
#  we have an dict expense which is stored in list
import datetime as dt
import math
expenses = []
print("welcome to expenses traker ")
while True :
    print("------------EXPENSES TRCKER------------")
    print("1. Add Expenses :")
    print("2. View All Expenses")
    print("3. View total spending")
    print("4. Exit")
    
    choice = int(input("enter no : "))
    
# add expenses
    if choice == 1 :
        date = input('date of spending : ')
        category = input(" Enter the category : ")
        description  = input("enter the description about your Expenses  : ")
        amount = float(input("enter amount that you spended : "))
        
        # taken detail from user now settle it into dict and add dict to expenses list
        expense = {
            "date":date  ,  
            "category" : category,
            "amount" :amount,
            "description" :description
        }
        expenses.append(expense) # here we added the list to maintai our expenses list
        print("--- Expense is added into Expenses ---")

    elif choice  == 2:
        if len(expenses) == 0:
            print("there is no expeses present so first spend some money.....")
        else:
            count = 1
            for eachSpend in expenses:
                print(f"your expense Number {count}:  ",expenses)
                count+=1

# viewing total amount you spended
    elif choice  ==  3:
        total = 0
        for totalamount in expenses:
            total += totalamount["amount"]
        print("total amount you spended is : ", total)
        
# exit
    elif choice == 4:
        print('thank you'.title())
        break
    
    else:
        print("................invalid number...............try again")