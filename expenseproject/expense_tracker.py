
from expenseclass import expense
import calendar
import datetime



def main():

    file_path='expensefile.csv'
    #get user expense
    expenses=get_user_expense()
    print(expenses)
    #write their expense to a file
    save_the_expenses(expenses,file_path)
    #read the file and summarize the expenses
    summarize_the_expenses(file_path,1000)

def get_user_expense():
    print(f'Running the user expenses')
    print('\n')
    expense_name=input("enter the expense name:")
    expense_amount=float(input("enter the expense amount:"))
    print(f'You have entered {expense_name},{expense_amount}')
    expense_category=['Food','Home','Work','Fun','Misc']
    
    while True:
        print("Select a category: ")
        for i,category in enumerate(expense_category):
            print(f' {i+1}. {category}')
        selected_index=int(input("Enter the category number: "))-1

        if selected_index in range(len(expense_category)):
            selected_category=expense_category[selected_index]
            new_expense=expense(name=expense_name,category=selected_category,amount=expense_amount)
                
            return new_expense

def save_the_expenses(expenses:expense,file_path):
    with open (file_path,'a') as f:
        f.write(f'{expenses.name},{expenses.amount},{expenses.category}\n')


def summarize_the_expenses(file_path,budget):
    expens:list[expense]=[]
    with open (file_path,'r') as f:
        lines=f.readlines()
        for line in lines:
            expense_name,expense_amount,expense_category=line.strip().split(",")
            line_expense=expense(name=expense_name,amount=float(expense_amount),category=expense_category)
            expens.append(line_expense)
    amount_by_category={}
    for exp in expens:
        key=exp.category
        if key in amount_by_category:
            amount_by_category[key]+= exp.amount
        else:
            amount_by_category[key]= exp.amount
    print('\n')
    print("Expenses by category: ")
    for category,amount in amount_by_category.items():
        print(f'{category}, ${amount:.2f}')
    
    total_spent=sum([i.amount for i in expens])
    print("You've spent ${total_spent:.2f} this month!")
    remaining_budget=budget-total_spent
    print(f"Budget remaining: ${remaining_budget:.2f}")

    now=datetime.datetime.now()
    days_in_month=calendar.monthrange(now.year,now.month)[1]
    remaining_days=days_in_month-now.day

    daily_budget=remaining_budget/remaining_days
    print(f"Budget per day: ${daily_budget:.2f}")




if __name__=='__main__':
    main()