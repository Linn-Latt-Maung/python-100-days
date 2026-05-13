def validate_isbn(isbn, length):
    # Fix the TypeError: len() takes only one argument
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    # Fix the off-by-one and IndexError:
    # main_digits should be the first (length - 1) digits
    main_digits = isbn[0:length - 1]
    # given_check_digit is the very last digit at index (length - 1)
    given_check_digit = isbn[length - 1]

    try:
        # Check for invalid characters while converting to integers
        main_digits_list = [int(digit) for digit in main_digits]
        
        if length == 10:
            expected_check_digit = calculate_check_digit_10(main_digits_list)
        else:
            expected_check_digit = calculate_check_digit_13(main_digits_list)

        if given_check_digit == expected_check_digit:
            print('Valid ISBN Code.')
        else:
            print('Invalid ISBN Code.')
            
    except ValueError:
        # Requirement: Handle non-numeric characters in the ISBN body
        print('Invalid character was found.')

def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    result = 11 - digits_sum % 11
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    result = 10 - digits_sum % 10
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def main():
    user_input = input('Enter ISBN and length: ')
    
    # Requirement: Handle missing commas (IndexError)
    try:
        values = user_input.split(',')
        if len(values) < 2:
            raise IndexError
            
        isbn = values[0].strip()
        
        # Requirement: Handle non-numeric length (ValueError)
        try:
            length = int(values[1].strip())
        except ValueError:
            print('Length must be a number.')
            return

        # Requirement: Fix IndentationErrors and validate range
        if length == 10 or length == 13:
            validate_isbn(isbn, length)
        else:
            print('Length should be 10 or 13.')
            
    except IndexError:
        print('Enter comma-separated values.')

# IMPORTANT: Comment out the call below for tests to run properly
# main()