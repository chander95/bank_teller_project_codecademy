checking_balance = 0
savings_balance = 0

#this function checks the balance of checking and savings accounts.
def check_balance(account_type, checking_balance, savings_balance):
    if account_type == "checking":
        balance = checking_balance
        balance_statement = f"Hello, Your {account_type} balance is {balance}.\n"
        return balance_statement
    elif account_type == "savings":
        balance = savings_balance
        balance_statement = f"Hello, Your {account_type} balance is {balance}.\n"
        return balance_statement
    else:
        return "Unsuccessful, please enter \"checking\" or \"savings\" \n"

#these function calls are just to ensure the function is working properly. It is.
print(check_balance("checking", checking_balance, savings_balance))
print(check_balance("savings", checking_balance, savings_balance))



#This function is used whenever a deposit needs to be made to a checking or savings account.
def make_deposit(account_type, amount, checking_balance, savings_balance):
    deposit_status = ""
    if float(amount) >= 0:
        if account_type == "checking":
            checking_balance += amount
            deposit_status = "successful"
            print(f"You made a deposit of ${amount} to your {account_type} account. Your new {account_type} account balance is ${checking_balance}. \n")
            return checking_balance
        elif account_type == "savings":
            savings_balance += amount
            deposit_status = "successful"
            print(f"You made a deposit of ${amount} to your {account_type} account. Your new {account_type} account balance is ${savings_balance}. \n")
            return savings_balance
        else:
            deposit_status = "unsuccessful, please enter checking or savings account. \n"
    else:
        print("unsuccessful, please enter an amount greater than 0. \n")
        return checking_balance, savings_balance

    deposit_statement = f"Deposit of ${amount} to your {account_type} account was {deposit_status}. \n" 
    print(deposit_statement)
    
    #return checking_balance
    #return savings_balance
    

#This line of code calls the deposit function and makes a deposit of $10.
savings_balance = make_deposit('savings', 10, checking_balance, savings_balance)

#This line of code checks the balance of the savings account after a deposit has been made.
print(check_balance('savings', checking_balance, savings_balance))

#This line of code calls the deposit function to make a deposit in the checking account of $100.
checking_balance = make_deposit("checking", 200, checking_balance, savings_balance)

#this line of code checks the balance of the checking account after the $200 deposit has been made.
print(check_balance('checking', checking_balance, savings_balance))



#this function is called whenever a withdrawal is being made from a checking or savings account.
def make_withdrawal(account_type, amount, checking_balance, savings_balance):
    withdrawal_status = ""
    fail = "Withdrawal unsuccessful, please enter amount less than balance.\n"
    withdrawal_statement = ""
    
    if account_type == 'checking' or account_type == 'savings':
        if account_type == "savings":
            if amount > savings_balance:
                print(fail)
            else:
                savings_balance -= amount
                withdrawal_status = 'successful'
                withdrawal_statement = f"Withdrawal of ${amount} from your {account_type} account was {withdrawal_status}. \n"
                return savings_balance
        elif account_type == 'checking':
            if amount > checking_balance:
                print(fail)
            else:
                checking_balance -= amount
                withdrawal_status = 'successful'
                withdrawal_statement = f"Withdrawal of ${amount} from your {account_type} account was {withdrawal_status}. \n"
                return checking_balance
        else:
            withdrawal_status = print("Unsuccessful, please enter \"checking\" or \"savings\" \n")
    
    #withdrawal_statement = f"Withdrawal of ${amount} from your {account_type} account was {withdrawal_status}."
    #print(withdrawal_statement)
    return savings_balance, checking_balance
                
#this line of code calls the withdrawal function and makes a savings withdrawal - withdraw will be unsuccessful since there is only $10
savings_balance, checking_balance = make_withdrawal('savings', 11, checking_balance, savings_balance)

#this line of code prints the savings account balance after the withdrawal has been made - should be $10
print(check_balance('savings', checking_balance, savings_balance))

#this line of code withdraws $170 from the checking account - new checking total is $30.
checking_balance = make_withdrawal('checking', 170, checking_balance, savings_balance)

#This line of code checks the checking account balance after the $170 withdrawal - should be $30.
print(check_balance('checking', checking_balance, savings_balance))



def acc_transfer(acc_from, acc_to, amount, checking_balance, savings_balance): 
    transaction_status = ""
    trans_error = "unsuccessful, please enter amount less than "
    if acc_from == 'savings' and acc_to == 'checking':
        if amount < savings_balance:
            savings_balance -= amount
            checking_balance += amount
            transaction_status = 'successful'
        else:
            transaction_status = f"{trans_error} {savings_balance}"
    elif acc_from == 'checking' and acc_to == 'savings':
        if amount < checking_balance:
            checking_balance -= amount
            savings_balance += amount
            transaction_status = 'successful'
        else:
            transaction_status = f"{trans_error} {checking_balance}"
    else:
        transaction_status = "unsuccessful, please enter \"checking\" or \"savings\""
    transaction_statement = f"Transfer of ${amount} from your {acc_from} account to your {acc_to} account was {transaction_status} \n"
    print(transaction_statement)
    return savings_balance, checking_balance
    

#this line of code takes $20 from the checking account and transfers it to the savings account
savings_balance, checking_balance = acc_transfer('checking', 'savings', 20, checking_balance, savings_balance)

#this line of code prints the new checking account balance after the $20 was transferred over to the savings account - should be $10
print(check_balance('checking', checking_balance, savings_balance))
    
#this line of code prints the savings account balance after the $20 checking transfer - should be $30.
print(check_balance('savings', checking_balance, savings_balance))

#this line of code takes $5 from the savings account and adds it to the checking account balance - should make checking balance $15
savings_balance, checking_balance = acc_transfer('savings', 'checking', 5, checking_balance, savings_balance)

#this line of code prints the checking account balance after the $5 savings transfer - should be $15
print(check_balance('checking', checking_balance, savings_balance))
    
#this line of code prints the savings account balance after the $5 transfer to checking account - should be $25.
print(check_balance('savings', checking_balance, savings_balance))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


