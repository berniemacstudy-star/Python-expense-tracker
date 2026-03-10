import json
from datetime import datetime #Adds a timestamp to JSON to make my payload feel real-world

def getExpenses():  # Function called getExpenses

    expenses = {}  # Unassigned Array of expenses, only dictionary, words, key values

    while True:  # Prompt user input
        item = input("Enter expense name or ('done'): ")

        if item == "done":
            break  # Can only use break in for or while loops

        try: # In case user types in nonsense
        
            cost = float(input("Enter cost of expense: "))  # Prompt input number to accomodate decimals
            
            expenses[item] = cost
            
        except ValueError:
            print("Enter a valid number!")  # Error Handling

    return expenses  # Store expenses


def financialAdvice(expenses):  # Function to provide user with "A.I" advice
    total = sum(expenses.values())  # Calculate the total

    if total > 10000:
        return "Your spending is too excessive. Consider cutting down costs!"
        
    elif total < 5000:
        return "Your spending is too limited. You are putting too much effort on savings!"
        
    else:
        return "Your spending is properly distributed. Good discipline!"

def displaySummary(expenses):  # Funtion abt net expense ratio to a single expense
    total = sum(expenses.values())  # Still need to calculate total again. It's a different function

    if total == 0:  # Prevents division by zero
        print("Total cannot be zero")
        return  # Stops function since the total was ZERO

    print("\nExpense breakdown")
    for item, cost in expenses.items():
        percentage = (cost / total) * 100
        print(f"{item}: ({percentage:.1f})% of total")

    print(f"\nTotal: R{total}")


def salarySavings(expenses):
    total = sum(expenses.values())
    
    incomes = []#Array of numbers

    while True:
            
            entry = input("Enter monthly income/s or ('done'): ")
            
            if entry == "done":
                  break
                  
            try:
                     income = float(entry)
                     incomes.append(income)
                       
            except ValueError:
                      print("Invalid income entered!")
                      
                      return
        
    incomeTot =  sum(incomes) #Sum of the multiple incomes

    savings = incomeTot - total
    
    # Savings should not equal or be less than zero warning
    if savings <= 0:
        print("You have no savings!")
        return
    
    #To let the variable savings return values, instead of just saying savings = null, JSON needs to return data, not print outputs
    return incomeTot, savings

# This function will later send data to an A.I API.
# This is where I will practically learn to create in JSON
# One step closer to achieving sufficient competency in coding, thus monetising it.

# Project goal:
# Build real-world coding competency that can be monetised through automation,
# data handling, and AI-powered services. 23/02/2026


def expensesToJSON(expenses, incomeTot, savings): #converts python dictionary to json string
#This function is a API ready strucured payload design
    
     total = sum(expenses.values()) 
     
     current_time = datetime.now().strftime("%Y -%m-%d %H:%M:%S")
     
     payload = {
     
     "timestamp":
         
         current_time,
     
     "user":
          { 
          
          "currency":
              "ZAR",
          },
     
     "financialSummary":
         { 
         
         "totalExpenses":
             total,
             
             "numberOfItems":
                 len(expenses)
         },
         
         "expenses":
             expenses,
         
         "advice":
             financialAdvice(expenses),#To pass the fS function to it's result  
             
          "incomeTotal":
              incomeTot, #This is just the result, it's obtained from the savings function
          
          "savings":
              savings

     }
     
     return json.dumps(payload, indent=4)
     

def saveJSONToFile(json_data):#This generates a separatejson file/data
#This is now a real artifact
    
    with open("financial_report.json", "w", encoding="utf-8") as file: #Always define encoding, utf, when writing files
        
        file.write(json_data)

if __name__ == "__main__":
    
    print("=== Personal Expense Tracker ===")
    
    expenses = getExpenses()  # Calls the getExpenses() function

    if not expenses:# Error message placed   here so that NO other function runs if this is the case
        print("No expenses entered!")
    else:
        print("\nA.I Advisor: ")
        print(financialAdvice(expenses))
        
        displaySummary(expenses)
        
        result = salarySavings(expenses)
        
        income = 0
        savings = 0
        
        if result:
            incomeTot,  savings = result
        
            print("\nSalary savings")
            print(f"Total income: R{incomeTot}")
            print(f"Savings: R{savings}")
      
            json_output = expensesToJSON(expenses, incomeTot, savings)
        
            print("\nJSON Output")
            print(json_output)
        
            saveJSONToFile(json_output)
            print("Financial report saved as financial_report.json")

#Add multiple incomes user input next time: Today date = 27/02

#Today's date, a fresh start again = 04/03: Wednesday recovery session complete, next goal: Improve on json, api, python.

#error @ line 169 solved