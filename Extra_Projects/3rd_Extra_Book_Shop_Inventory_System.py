def find_book_index(inventory, book_title, genre):
    for index, book in enumerate(inventory):
        if book[0] == book_title and book[1] == genre:
            return index
    return -1

def add_new_book(inventory, book_title, genre, quantity, price):
    if find_book_index(inventory, book_title, genre) != -1:
        return 'Error: Book already exists in inventory.'
    if quantity < 0:
        return 'Error: Quantity cannot be negative.'
    if price < 0:
        return 'Error: Price cannot be negative.'
    inventory.append([book_title, genre, quantity, price])
    return 'Success: ' + book_title + ' added to inventory.'

def restock_book(inventory, book_title, genre, quantity):
    if quantity <= 0:
        return 'Error: Restock quantity must be greater than zero.'
    if find_book_index(inventory, book_title, genre) == -1:
        return 'Error: Book does not exist in inventory.'
    inventory[find_book_index(inventory, book_title, genre)][2] += quantity
    return 'Success: ' + book_title + ' restocked. New quantity is ' + str(inventory[find_book_index(inventory, book_title, genre)][2]) + '.'

def sell_book(inventory, book_title, genre, quantity):
    if quantity <= 0:
        return 'Error: Sale quantity must be greater than zero.'
    if find_book_index(inventory, book_title, genre) == -1:
        return 'Error: Book does not exist in inventory.'
    if inventory[find_book_index(inventory, book_title, genre)][2] < quantity:
        return 'Error: Insufficient stock to complete sale.'
    inventory[find_book_index(inventory, book_title, genre)][2] -= quantity
    return 'Success: ' + book_title + ' sold. New quantity is ' + str(inventory[find_book_index(inventory, book_title, genre)][2]) + '.'

def print_inventory_report(inventory):
    total_inventory_value = 0
    report_string = 'BOOK INVENTORY REPORT:\n'
    
    for book in inventory:
        title = book[0]
        genre = book[1]
        quantity = book[2]
        price = book[3]
        total_value = quantity * price
        total_inventory_value += total_value
        report_string += f'Book: {title} | Genre: {genre} | Quantity: {quantity} | Price: ${price} | Total Value: ${total_value}\n'

    report_string += f'------------------------------\n'
    report_string += f'Total Inventory Value: ${total_inventory_value}'
    
    return report_string

# 1. Create the empty inventory
book_shop_inventory = []

# 2. Add books
print("--- INVENTORY UPDATES ---")
print(add_new_book(book_shop_inventory, 'The Great Gatsby', 'Fiction', 5, 10.00))
print(add_new_book(book_shop_inventory, 'A Brief History of Time', 'Science', 3, 15.00))
print(add_new_book(book_shop_inventory, 'The Great Gatsby', 'Fiction', 2, 10.00)) # Should trigger "already exists" error

# 3. Restock and Sell
print("\n--- DAILY TRANSACTIONS ---")
print(restock_book(book_shop_inventory, 'The Great Gatsby', 'Fiction', 5)) # Gatsby stock should become 10
print(sell_book(book_shop_inventory, 'A Brief History of Time', 'Science', 1)) # Should reduce stock to 2
print(print_inventory_report(book_shop_inventory))

