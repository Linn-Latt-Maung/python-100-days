def find_item_index(inventory, item_name):
    for index, items in enumerate(inventory):
        if items[0] == item_name:
            return index
    return -1

def add_new_item(inventory, item_name, quantity, price):
    if find_item_index(inventory, item_name) != -1:
        return 'Error: Item already exists in catalog.'
    if quantity < 0:
        return 'Error: Quantity cannot be negative.'
    if price < 0:
        return 'Error: Price cannot be negative.'
    inventory.append([item_name, quantity, price])
    return 'Success: ' + item_name + ' added to catalog.'

def restock_item(inventory, items_name, quantity):
    if quantity <= 0:
        return 'Error: Restock quantity must be greater than zero.'
    if find_item_index(inventory, items_name) == -1:
        return 'Error: Item does not exist in catalog.'
    inventory[find_item_index(inventory, items_name)][1] += quantity
    return 'Success: ' + items_name + ' restocked. New quantity is ' + str(inventory[find_item_index(inventory, items_name)][1]) + '.'

def sell_item(inventory, item_name, quantity):
    if quantity <= 0:
        return 'Error: Sale quantity must be greater than zero.'
    if find_item_index(inventory, item_name) == -1:
        return 'Error: Item does not exist in catalog.'
    if inventory[find_item_index(inventory, item_name)][1] < quantity:
        return 'Error: Insufficient stock to complete sale.'
    inventory[find_item_index(inventory, item_name)][1] -= quantity
    total_price = quantity * inventory[find_item_index(inventory, item_name)][2]
    return 'Success: Sold ' + str(quantity) + ' of ' + item_name + '. Total price is $' + str(total_price) + '. New quantity is ' + str(inventory[find_item_index(inventory, item_name)][1]) + '.'

def print_inventory_report(inventory):
    total_inventory_value = 0
    report_string = 'INVENTORY REPORT:\n'
    
    for item in inventory:
        name = item[0]
        quantity = item[1]
        price = item[2]
        total_value = quantity * price
        total_inventory_value += total_value
        report_string += f'Item: {name} | Quantity: {quantity} | Price: ${price} | Total Value: ${total_value}\n'

    report_string += f'------------------------------\n'
    report_string += f'Total Inventory Value: ${total_inventory_value}'
    
    return report_string

# 1. Create the empty warehouse
tech_shop = []

# 2. Add products
print("--- CATALOG UPDATES ---")
print(add_new_item(tech_shop, 'Laptop', 10, 1000.00))
print(add_new_item(tech_shop, 'Mouse', 50, 20.00))
print(add_new_item(tech_shop, 'Mouse', 10, 20.00)) # Should trigger "already exists" error

# 3. Restock and Sell
print("\n--- DAILY TRANSACTIONS ---")
print(restock_item(tech_shop, 'Laptop', 5)) # Laptop stock should become 15
print(sell_item(tech_shop, 'Mouse', 60)) # Should trigger "Not enough stock" error
print(sell_item(tech_shop, 'Mouse', 2)) # Should succeed and say it sold for $40.0

# 4. Print the final report
print("\n" + print_inventory_report(tech_shop))
