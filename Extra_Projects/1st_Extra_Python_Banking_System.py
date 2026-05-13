def find_account_index(db, name):
    for index, account in enumerate(db):
        if account[0] == name:
            return index
    return -1

def create_account(db, name, initial_deposit):
    if type(name) is not str:
        return 'Error: Name must be a string.'
    if initial_deposit < 0:
        return 'Error: Deposit cannot be negative.'
    if find_account_index(db, name) != -1:
        return 'Error: Account already exists.'
        
    db.append([name, initial_deposit])
    return 'Success: Account created.'

def deposit(db, name, amount):
    if amount <= 0:
        return 'Error: Deposit must be greater than zero.'
        
    index = find_account_index(db, name)
    if index == -1:
        return 'Error: Account does not exist.'
    
    db[index][1] += amount
    return f'Success: New balance is ${db[index][1]}.'

def transfer(db, sender_name, receiver_name, amount):
    if amount <= 0:
        return 'Error: Transfer amount must be greater than zero.'
        
    sender_index = find_account_index(db, sender_name)
    receiver_index = find_account_index(db, receiver_name)
    
    if sender_index == -1:
        return 'Error: Sender account does not exist.'
    if receiver_index == -1:
        return 'Error: Receiver account does not exist.'
    if db[sender_index][1] < amount:
        return 'Error: Insufficient funds.'
    
    db[sender_index][1] -= amount
    db[receiver_index][1] += amount

    return f'Success: New balance for {sender_name} is ${db[sender_index][1]} and for {receiver_name} is ${db[receiver_index][1]}.'

def print_bank_report(db):
    total_bank_money = 0
    report_string = 'Bank LEDGER:\n'
    
    for account in db:
        name = account[0]
        balance = account[1]
        total_bank_money += balance
        report_string += f'Account: {name} | Balance: ${balance}\n'

    report_string += f'------------------------------\n'
    report_string += f'Total Bank Assets: ${total_bank_money}'
    
    return report_string

# ==========================================
# TESTING BLOCK - RUNS THE ACTUAL SYSTEM
# ==========================================

# 1. Create the empty database
my_bank = []

# 2. Run some tests and print the results to the terminal
print("--- INITIALIZING BANK ---")
print(create_account(my_bank, 'Sung', 1000.0))
print(create_account(my_bank, 'Jin', 200.0))

print("\n--- TRANSACTIONS ---")
print(deposit(my_bank, 'Sung', 500.0)) 
print(transfer(my_bank, 'Sung', 'Jin', 300.0)) 

# 3. Print the final report
print("\n" + print_bank_report(my_bank))
