def number_pattern(n):
    if type(n) is not int:
        return 'Argument must be an integer value.'
    if n <= 0:
        return 'Argument must be an integer greater than 0.'
        
    number_lists = []
    for num in range(1, 1 + n):
        number_lists.append(str(num))
        
    return ' '.join(number_lists)
