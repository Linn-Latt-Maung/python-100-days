def find_book_index(db, book_title):
    for index, book in enumerate(db):
        if book[0].lower() == book_title.lower():
            return index
    return -1

def run_library_system():
    library_db = [
        ['Book Title 1', 'Author A', 5, 10.00],
        ['Book Title 2', 'Author B', 3, 15.00],
        ['Book Title 3', 'Author C', 2, 20.00],
        ['Book Title 4', 'Author D', 0, 25.00]
    ]
    
    print("Welcome to the Meow Library System!")

    while True:
        print('\n' + '-'*30)
        print('Meow Library Menu:')
        print('\n' + '-'*30)
        print('1. View Library Catalog')
        print('2. Borrow a Book')
        print('3. Return a Book')
        print('4. Add a New Book')
        print('5. Exit')

        choice= input ('Please enter your choice (1-5): ')

        if choice == '1':
            print('\n ----- Current Library Catalog -----')
            for book in library_db:
                print(f'Title: {book[0]} | Author: {book[1]} | Available Copies: {book[2]}')
        
        elif choice == '2':
            book_title = input('Enter the title of the book you want to borrow: ')
            index = find_book_index(library_db, book_title)
            if index == -1:
                print('Error: Book not found in catalog.')
            elif library_db[index][2] <= 0:
                print('Sorry, that book is currently unavailable.')
            else:
                library_db[index][2] -= 1
                print(f'Success: You have borrowed "{library_db[index][0]}". Enjoy reading!')

        elif choice == '3':
            book_title = input('Enter the title of the book you want to return: ')
            index = find_book_index(library_db, book_title)
            if index == -1:
                print('Error: Book not found in catalog.')
            else:
                library_db[index][2] += 1
                print(f'Thank you for returning "{library_db[index][0]}". We hope you enjoyed it!')
        
        elif choice == '4':
            book_title = input('Enter the title of the new book: ')
            author = input('Enter the author of the new book: ')

            quantity_input = input('Enter the quantity of the new book: ')

            if quantity_input.isdigit():
                quantity = int(quantity_input)\
                
                if find_book_index(library_db, book_title) != -1:
                    print('Error: Book already exists in catalog.') 
                else:
                    library_db.append([book_title, author, quantity]) 
                    print(f'Success: "{book_title}" by {author} added to the catalog with {quantity} copies.')
            else:
                print('Error: Quantity must be a whole number.')
                

  

        elif choice == '5':
            print("Thank you for using the Meow Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

run_library_system()
