# daily-learning-log
coding 100 days of Python

{

Date - 4/16/2026
================

Pandas and NumPy for Data Analysis
TensorFlow and Scikit for ML and AI model

In Web Development - Django, FastAPI, and Flask (Python Framework for building scalable and secure back-end with minimal effort)

In Cybersecurity - to detect vulnerabilities like malware and other viruses and can build automated security scans and analyze threats

In DevOps (software development methodology) - for writing CI/CD scripts and managing infrastructure across development pipelines. It is also commonly used to build back-end services and internal APIs.

In Software Testing - Using pytest

For UI and manage Cloud Deployments for project - Selenium and BeautifulSoup libraries use


================================

1st - Variables and Data Types
------------------------------

eg 1 

- print('My favorite colors are', 'blue', 'green', 'red')
output : My favorite colors are blue green red

Cuz - Python automatically adds a space between each item when you separate them with commas. This is helpful when you want to print several pieces of information together.
    
  
------------------------------------------

here's are all the data types covered in this lesson, along with their types in the terminal:

my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>

----------------------------------------------

The built-in isinstance() function lets you check if a variable matches a specific data type. It takes in an object and the type you want to check it against, then returns a boolean. Here are some examples:

isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('John Doe', int) # False

==================================================================

2nd -  Introduction to Strings
------------------------------

-> If you need a multi-line string, you can use triple double quotes or single quotes:

Example Code

my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''

-> If your string contains either single or double quotation marks, then you have two options -

-->   Use the opposite kind of quotes. That is, if your string contains single quotes, use double quotes to wrap the string, and vice versa:

Example Code

msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

-->  Escape the single or double quotation mark in the string with a backslash (\). With this method, you can use either single or double quotation marks to wrap the string itself:

Example Code

msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

-> And you have to check if you have a lot of quot - 

Example Code

my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False


-> If you want to count length

Example Code

my_str = 'Hello world'
print(len(my_str))  # 11

-> If you want position call -

Example Code

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1])  # d
print(my_str[-2]) # l

-> Python doesn't draw a hard line between those two groups. Instead, all data gets treated as objects, and some objects are immutable while others are mutable. Immutable data types can't be modified or altered once they're declared. You can point their variables at something new, which is called reassignment, but you can't change the original object itself by adding, removing, or replacing any of its elements.

	Strings are immutable data types in Python. This means that you can reassign a different string to a variable:

Example Code

greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

But direct modification of a string isn't allowed

Example Code

greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment

---------------------------------------------------------

What Are String Concatenation and String Interpolation?
-------------------------------------------------------

-> string concatenation (+)

Example Code

my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World


if Example Code

name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age) # TypeError: can only concatenate str (not "int") to str

--> But can change type

Example Code

name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26


--> And you can also use augmented assignment operator (+=)

Example Code

name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26



-> string interpolation (F-string with {})

Example Code
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

---------------------------------------------------------

What Is String Slicing and How Does It Work?
-------------------------------------------------------


In a previous lesson, you learned how each character in a string can be identified by its index (starting from zero), and accessed using the bracket notation:

Example Code

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1]) # d

-> String slicing lets you extract a portion of a string or work with only a specific part of it. Here's the basic syntax:

Example Code

string[start:stop]

-> If you want to extract characters from a certain index to another, you just separate the start and stop indices with a colon:

Example Code

my_str = 'Hello world'
print(my_str[1:4]) # ell

Note that the stop index is non-inclusive, so [1:4] just extracted the characters from index 1, and up to, but not including, the character at index 4.


-> You can also omit the start and stop indices, and Python will default to 0 or the end of the string, respectively. For example, here's what happens if you omit the start index:

Example Code

my_str = 'Hello world'
print(my_str[:7])  # Hello w

-> This extracts everything from index 0 up to (but not including), the character at index 7. And here's what happens if you omit the stop index:

Example Code

my_str = 'Hello world'
print(my_str[8:])  # rld

This extracts everything from the character at index 8 until the end of the string.


Note that slicing a string does not modify the original string:

Example Code

my_str = 'Hello world'
print(my_str[8:])  # rld
print(my_str)  # Hello world

-> You can also omit both the start and stop indices, which will extract the whole string:

Example Code

my_str = 'Hello world'
print(my_str[:])  # Hello world

-> Apart from the start and stop indices, there's also an optional step parameter, which is used to specify the increment between each index in the slice.

Here's the syntax for that:

Example Code

string[start:stop:step]

-> In the example below, the slicing starts at index 0, stops before 11, and extracts every second character:

Example Code

my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd

-> A helpful trick you can do with the step parameter is to reverse a string by setting step to -1, and leaving start and stop blank:

Example Code

my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH

---------------------------------------------------------

What Are Some Common String Methods?
-------------------------------------------------------

upper(): Returns a new string with all characters converted to uppercase.

Example Code

my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

lower(): Returns a new string with all characters converted to lowercase.

Example Code

my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world

strip(): Returns a new string with the specified leading and trailing characters removed. If no argument is passed it removes leading and trailing whitespace.

Example Code

my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"

replace(old, new): Returns a new string with all occurrences of old replaced by new.

Example Code

my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world

split(separator): Splits a string on a specified separator into a list of strings. If no separator is specified, it splits on whitespace.

Example Code

my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']

join(iterable): Joins elements of an iterable into a string with a separator.

Example Code

my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world

startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix.

Example Code

my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True

endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.

Example Code
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True

find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one.

Example Code

my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6

count(substring): Returns the number of times a substring appears in a string.

Example Code

my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2

capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.

Example Code

my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world

isupper(): Returns True if all letters in the string are uppercase and False if not.

Example Code

my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False

islower(): Returns True if all letters in the string are lowercase and False if not.

Example Code

my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True

title(): Returns a new string with the first letter of each word capitalized.

Example Code

my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World


}

{

Date - 4/17/2026
================

How Do You Work With Integers and Floating Point Numbers? (Numbers and Mathematical Operations)
---------------------------------------------------------

(+)  for addition
(-)  for subtraction
(*)  for multiplication
(/)  for division
(%)  for remainder
(//) for Floor Division !That output will be integer division
(**) for power

-> Floor Division Example -

my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0


-> round(): Rounds a number to the specified number of decimal places. By default this function rounds to the nearest integer, and returns a whole number with no decimal places:

my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3

-> abs(): returns the absolute value of a number,

num = -15

absolute_value = abs(num)
print(absolute_value) # 15

-> pow(): raises a number to the power of another or performs modular exponentiation.

result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3

-----------------------------------------------------------------------

How Do Augmented Assignments Work? (Numbers and Mathematical Operations)
----------------------------------

Main - 

The basic syntax of an augmented assignment looks like this:

variable <operator>= value

Which is a more efficient way of doing this:

variable = variable <operator> value

---------------------------------

+= , -=, *=, /=, //=, %=, *rrinn*=

---------------------------------

-> You can use some augmented assignment operators with strings.

Example Code

greet = 'Hello'
greet += ' World'

print(greet) # Hello World

--> And the multiplication assignment operator can be used to repeat a string

greet = 'Hello'
greet *= 3

print(greet) # HelloHelloHello

----------------------------------

Increment and decrement operators (++ and --) -> They are not work in Python

Example Code - 

my_var = 5

print(+my_var)   # 5
print(++my_var)  # 5
print(+++my_var) # 5

my_var += 1

print(my_var) # 6

===========================================================

How Do Conditional Statements and Logical Operators Work? (Booleans and Conditionals)
---------------------------------------------------------

(==) for Equal
(!=) for Not Equal
(>)  for Greater than
(<)  for Less than
(>=) for Greater than or equal
(<=) for Less than or equal

-----------------------------------------------------------

if / eif / else
---------------

if condition1:
   pass # Code to execute if condition1 is True
elif condition2:
   pass # Code to execute if condition1 is False and condition2 is True
else:
   pass # Code to execute if all conditions are False


Example Code

age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant

===========================================================

What Are Truthy and Falsy Values, and How Do Boolean Operators and Short-Circuiting Work? (Booleans and Conditionals)
-------------------------------------------------------------------------------------------

For Boolean
-----------

True Value - True, Integer (1), String ('something include')

False Value - None, False, Integer (0), Float (0.0), String ('')


Example Code

print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True

-----------------------------------------------------
(and) operator 
--------------

if condition_1 and condition_2:
   pass
else:
   pass

-> need to correct both condition

(or) operator
--------------

if condition_1 or condition_2:
   pass
else:
   pass

-> need to correct only one condition 


(not) operator
--------------

Example Code

print(not '')      # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0)       # True, because 0 is falsy
print(not 1)       # False, because 1 is truthy
print(not False)   # True, because False is falsy
print(not True)    # False, because True is truthy


Example Code

is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')

-> Since is_admin is False, then not is_admin is saying not False which is True. So the message Access denied for non-administrators. will be printed.

}


{

Date - 4/18/2026
================

How Do Functions Work in Python? (Understanding Functions and Scope)
--------------------------------

input() Function
----------------

name = input('What is your name?') # User types "Kolade" and presses Enter  
print('Hello', name) # Output: Hello Kolade

----------------------------------------

int() Function
--------------

print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 

----------------------------------------

def function
------------

-> You can also write your own custom functions.

Format - def nameoffunction():
             pass


Example Code -

def hello():
    print('Hello World')

To run the function, you need to call it with its name followed by a pair of parentheses:

Example Code

hello() # Hello World



Another Example Code - 

def calculate_sum(a,b):
    print(a+b)

-> You can see that our function, calculate_sum, has a and b in its parentheses, separated by a comma. Those are called parameters. Think of parameters as placeholder variables that act as "slots" for the values you pass into functions when you call them.

-> To use the parameters, you have to pass in "arguments". Arguments are the values you pass to a function when you call it.

Here's how to call the calculate_sum function to sum together the numbers 3 and 1:

To run:

calculate_sum(3,1) # 4

------------------------------------

-> Functions also use a special return keyword to exit the function and return a value. If you don't explicitly use return, Python will return None by default.


Example Code

def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None


-> You can see that the calculate_sum function prints the sum of a and b, but it doesn't return anything explicitly. So when we assign its result to my_sum, the value is actually None. To fix that, you can use the return keyword to send back the result:

Example Code

def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum) # 4

Now, calculate_sum returns the sum of a and b, which gets stored in my_sum.

---------------------------------------

What Is Scope in Python and How Does It Work? (Understanding Functions and Scope)
---------------------------------------------

There are 4 types of scope - LEGB 

Local Scope
Enclosing Scope
Global Scope
Built-in Scope

-> Python uses the LEGB rule to resolve the scope of the variables in your program.

------------------------------------

Local Scope 
-----------

Local scope means that a variable declared inside a function or class can only be accessed within that function or class.

Here's an example:

def my_func():
    my_var = 10
    print(my_var)

-> In this case, the my_func function has its own scope which cannot be accessed from outside the function. Calling my_func will output 10, but printing my_var outside the function will lead to a NameError:

def my_func():
    my_var = 10 # Locally scoped to my_func
    print(my_var)

my_func() # 10

print(my_var) # NameError: name 'my_var' is not defined

------------------------------------

Enclosing Scope
---------------

Enclosing scope means that a function that's nested inside another function can access the variables of the function it's nested within.

For example:

def outer_func():
    msg = 'Hello there!'
    def inner_func():
        print(msg)
    inner_func()

outer_func() # Hello there!

-> In this example, the inner function, inner_func, can freely access the msg variable defined in the outer function, outer_func. However, note that outer functions cannot access variables defined within any nested functions:

def outer_func():
    msg = 'Hello there!'
    print(res)
    def inner_func():
        res = 'How are you?'
        print(msg)
    inner_func()

outer_func() # NameError: name 'res' is not defined

-> That's because res is locally scoped to inner_func. Also, notice that outer_func tries to print res before inner_func is called.

-> One solution is to initialize res as an empty string in the enclosing scope, which is within outer_func. Then within inner_func, make res a non-local variable with the nonlocal keyword:

def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope
    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()
    inner_func()
    print(res)  # Now res is accessible and modified

outer_func()

# Output:
# Hello there!
# How are you?


------------------------------------

Global Scope
------------

Global scope refers to variables that are declared outside any functions or classes which can be accessed from anywhere in the program. Here, my_var can be accessed anywhere, even inside a function it's not defined in:

my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100

-> And if you want to make a locally scoped variable defined inside a function globally accessible, you can use the global keyword:

my_var_1 = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars() # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var_2) # 10

-> You can also use the global keyword to modify a global variable:

my_var = 10  # A global variable

def change_var():
    global my_var  # Allows modification of a global variable
    my_var = 20

change_var()

print(my_var)  # my_var is now modified globally to 20

------------------------------------

Build-in Scope
--------------

print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False

}


{

Date - 4/19/2026
================

What are Lists and How Do They Work? (Working with Loops and Sequences)
------------------------------------

Core Concepts

Definition: An ordered, mutable sequence that can contain mixed data types.

-> Creation: Use square brackets or the list() constructor.

Example Code

cities = ['Los Angeles', 'London', 'Tokyo']
letters = list('abc') # ['a', 'b', 'c']

-> Length: Use len() to find the total number of items.

Example Code

len(cities) # Returns 3

Accessing & Slicing (Zero-based Indexing)
-----------------------------------------

-> Positive Indexing: Grabs items from the start (first item is 0).

Example Code

cities[0] # 'Los Angeles'


-> Negative Indexing: Grabs items from the end (last item is -1).

Example Code

cities[-1] # 'Tokyo'

-> Nested Lists: Access items using multiple brackets.

Example Code

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2][1] # 'Rust' (Index 2 is the sub-list, index 1 is 'Rust')

-> Slicing ([start:stop:step]): Extracts a portion (the stop index is not included).

Example Code

numbers = [1, 2, 3, 4, 5, 6]
numbers[1:4]  # [2, 3, 4]
numbers[1::2] # [2, 4, 6] (Starts at index 1, skips every other item)

Modifying Lists
---------------

-> Update: Assign a new value directly to an index.

Example Code

langs = ['Python', 'Java', 'C++']
langs[0] = 'JavaScript'  # ['JavaScript', 'Java', 'C++']

-> Delete: Use the del keyword.

Example Code

del langs[1]  # ['JavaScript', 'C++']

Useful Operators
----------------

-> in keyword: Checks if an item exists in the list.

Example Code

programming_languages = ['Python', 'Java', 'C++', 'Rust']

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False

Sometimes it is common to have lists nested inside of other lists like this:

Example Code

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]

In this example, we have one nested list containing three popular programming languages. To access the nested list, you will need to access it using index 2 since lists are zero based indexed:

Example Code

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2] # ['Python', 'Rust', 'C++']

Then to access the second language from that nested list, you will need to access it using index 1 like this:

Example Code

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2][1] # 'Rust'

-> Unpacking: Assigns list items directly to individual variables.

Example Code

developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

-> Asterisk (*) Operator: If you need to collect any remaining elements from a list, you can use the asterisk (*) operator like this:

Example Code

developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

-> The last concept we will look at is the slice operator (:). Similar to strings, you can access portions of a list by using the slice operator like this:

Example Code

desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
desserts[1:4] # ['Cookies', 'Ice Cream', 'Pie']

-> If you wanted to extract a list of just even numbers, you can use the slicing operator like this:

Example Code

numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2] # [2, 4, 6]

--------------------------------------------------

What are Lists and How Do They Work? (Working with Loops and Sequences)
------------------------------------

append() method
---------------

Example Code

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]

Example Code

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]

-------------------------
extend() method
---------------

Example Code

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]

-------------------------
insert() method
---------------

Example Code

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)

print(numbers) # [1, 2, 2.5, 3, 4, 5]

-------------------------
remove() method
---------------

Example Code

numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)

print(numbers) # [10, 20, 30, 40, 50]

-> It is important to note that this method will only remove the first occurrence of an item. Not all of them:

Example Code

numbers = [10, 20, 30, 40, 50, 50, 50]
numbers.remove(50)

print(numbers) # [10, 20, 30, 40, 50, 50]

-------------------------
pop() method
------------

To remove an element at a specific index in the list, you can use the pop() method like this:

Example Code

numbers = [1, 2, 3, 4, 5]
numbers.pop(1) # The number 2 is returned

-> If you don't specify an element for the pop method, then the last element is removed.

Example Code

numbers = [1, 2, 3, 4, 5]
numbers.pop() # The number 5 is returned

-------------------------
clear() method
--------------

Example Code

numbers = [1, 2, 3, 4, 5]
numbers.clear()

print(numbers) # []

-------------------------
sort() method
--------------

Example Code

numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers) # [1, 2, 19, 35, 41, 67]

-> In contrast to the sort() method, there is the sorted() function which works for any iterable and returns a new sorted list instead of modifying the original list. 

Example Code

numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]

-------------------------
reverse() method
----------------

Example Code

numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers) # [1, 2, 3, 4, 5, 6]

-------------------------
index() method
---------------

Example Code

programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java') # 1

-> If you put wrong or not exist element, will show ValueError

========================================================



}

{


Date - 4/20/2026
================

What Are Tuples and How Do They Work? (Working with Loops and Sequences)
--------------------------------------

A tuple is a Python data type used to create an ordered sequence of values. Tuples are similar to lists, but while lists are a mutable data type, tuples are immutable. This means that the elements in a tuple cannot be changed once it's created. Tuples can contain a mixed set of data types like this:

developer = ('Alice', 34, 'Rust Developer')

If example code - 

programming_languages = ('Python', 'Java', 'C++', 'Rust')
programming_languages[0] = 'JavaScript'

Will show TypeError

-> To access an element from a tuple, you can use bracket notation and the index number:

developer = ('Alice', 34, 'Rust Developer')
developer[1] # 34

-> Another way to create a tuple is by using the tuple() constructor like this:

developer = 'Jessica'
tuple(developer) # ('J', 'e', 's', 's', 'i', 'c', 'a')

-> To check if an item is in a tuple, you can use the in keyword like this:

programming_languages = ('Python', 'Java', 'C++', 'Rust')

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False

-> You can also unpack items from a tuple just like you did with lists:

developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'


-> If you need to collect any remaining elements from a tuple, you can use the asterisk (*) operator like this:

developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

-> Just like with a list, you can use the slice operator on a tuple to extract a portion of it. Here is an example of extracting the items 'pie' and 'cookies' into a separate tuple:

desserts = ('cake', 'pie', 'cookies', 'ice cream')
desserts[1:3] # ('pie', 'cookies')

-------------------------------------------------

What Are Some Common Methods for Tuples? (Working with Loops and Sequences)
-----------------------------------------

count() Methods
---------------

Example Code - 1

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust') # 2

Example Code - 2

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('JavaScript') # 0

Example Code - 3

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count()

Will show TypeError

----------------------------
index() Methods
---------------

Example Code - 1

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('Java') # 1

Example Code - 2

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('JavaScript')

Will show ValueError

Example Code - 3

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3) # 5

In this example, we are specifying where to start searching for the string Python. By passing in the number 3 as the second argument to the index() function, we are specifying to start searching at index 3. Since Python appears twice in the tuple, the index() function will return index 5 instead of index 2 because of the use of the optional start index argument.

Example Code - 4

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
programming_languages.index('Python', 2, 5) # 2

Now the result is index 2 because we are starting the search at index 2, and searching up to, but not including, index 5.

----------------------------
sorted() Methods
---------------

sorted() for int or float
-------------------------

numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers) # [2, 3, 7, 13, 18, 45, 67, 78]

sorted() for String
--------------------

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted(programming_languages, key=len)

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

-------------------------------------------------

How Do Loops Work? (Working with Loops and Sequences)
------------------

for loop
--------

Example Code

programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)

-- The result would be:

Rust
Java
Python
C++

--> Notice that the print(language) is indented inside of the loop. Without that indentation, you would get an IndentationError.

Another Example Code

for char in 'code':
    print(char)

-- The result would be:

c
o
d
e

-> Just like in JavaScript, you can also nest for loops in Python. Here is an example of using a nested for loop:

Example Code

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

--> The outer loop will iterate through each category in the categories list. For each category, the inner loop will iterate through each food in the foods list. Here is the result that will be printed to the console:

Fruit Apple
Fruit Carrot
Fruit Banana
Vegetable Apple
Vegetable Carrot
Vegetable Banana

-----------
while loop
----------

Example Code

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')

--> In this example we have a secret_number variable with the value of 3 and an initial guess of 0. Then we use the input function to get input from the user, then convert the input string into an integer with the int() function, and assign it to the guess variable. If the user guesses correctly by inputting 3, the while loop is broken out of and the message You got it! is printed to the console. Otherwise, the message Wrong! Try again. is printed to the console, and the loop repeats, prompting the user to guess again.

Here's an example result:

Guess the number (1-5): 2
Wrong! Try again.
Guess the number (1-5): 1
Wrong! Try again.
Guess the number (1-5): 3
You got it!

--------------------

break and continue
------------------

break example code - 

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)

-- result 

#Jess (cuz when developer variable see Naomi, the program break)



continue example code -

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)

-- result

#Jess, Tom (cuz when developer variable see Naomi, the program skip that Naomi because of using continue)

--------------------

with else (work both with for and while)
---------

Example Code 

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")


--> In this example we have a list of random words, and a for loop is used to loop through each word. Inside the outer for loop, we have another for loop to loop through each letter of each word. If the lowercase version of the letter is a vowel, we print the word followed by what vowels it contains, then break out of the inner loop. If the word contains no vowels, then we print a message indicating that.

-- the result looks like in the console:

'sky' has no vowels
'apple' contains the vowel 'a'
'rhythm' has no vowels
'fly' has no vowels
'orange' contains the vowel 'o'





}



{


Date - 4/21/2026
================

What Are Ranges and How Can You Use Them in a Loop? (Working with Loops and Sequences)
---------------------------------------------------

range() function
----------------

The range() function is used to generate a sequence of integers.

range(start, stop, step)

Example Code - 1
 
for num in range(3):
    print(num)

#0,1,2


Example Code - 2

for num in range(1, 5):
    print(num)

#1,2,3,4

Example Code - 3

for num in range(2, 11, 2):
    print(num)

#2,4,6,8,10

Example Code - 4

for num in range():
    print(num)

-- result will show error with TypeError: range expected at least 1 argument, got 0

Example Code - 5

for num in range(3.4):
    print(num)

-- result will show error with TypeError: 'float' object cannot be interpreted as an integer

Example Code - 5

for num in range(40, 0, -10):
    print(num)

#40,30,20,10

Example Code - 6

numbers = list(range(2, 11, 2))
print(numbers) # [2, 4, 6, 8, 10]

----------------------------------------------------------------

What Are the Enumerate and Zip Functions and How Do They Work? (Working with Loops and Sequences)
--------------------------------------------------------------

In previous lessons you learned how to work with the for loop, which is used to repeat a block of code a set number of times.  if you wanted to keep track of the index for each element? Well, one option is to create an index variable and increment it by 1 for each iteration of the loop. For Example -


languages = ['Spanish', 'English', 'Russian', 'Chinese']

index = 0

for language in languages:
    print(f'Index {index} and language {language}')
    index += 1


emumerate() function
--------------------

Example Code 

languages = ['Spanish', 'English', 'Russian', 'Chinese']

list(enumerate(languages))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

--> so with above for example -

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

#
Index 0 and language Spanish
Index 1 and language English
Index 2 and language Russian
Index 3 and language Chinese

If we want to start at 1 not 0 -

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')

#
Index 1 and language Spanish
Index 2 and language English
Index 3 and language Russian
Index 4 and language Chinese

----------------------

zip() function
--------------

Example Code

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

list(zip(developers, ids))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

--> Example with for looping 

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')

#
Name: Naomi
ID: 1
Name: Dario
ID: 2
Name: Jessica
ID: 3
Name: Tom
ID: 4

------------------------------------------------

What Are the Enumerate and Zip Functions and How Do They Work? (Working with Loops and Sequences)
--------------------------------------------------------------

In previous lessons you learned how to work with the for loop, which is used to repeat a block of code a set number of times.  if you wanted to keep track of the index for each element? Well, one option is to create an index variable and increment it by 1 for each iteration of the loop. For Example -


languages = ['Spanish', 'English', 'Russian', 'Chinese']

index = 0

for language in languages:
    print(f'Index {index} and language {language}')
    index += 1


emumerate() function
--------------------

Example Code 

languages = ['Spanish', 'English', 'Russian', 'Chinese']

list(enumerate(languages))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

--> so with above for example -

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

#
Index 0 and language Spanish
Index 1 and language English
Index 2 and language Russian
Index 3 and language Chinese

If we want to start at 1 not 0 -

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}')

#
Index 1 and language Spanish
Index 2 and language English
Index 3 and language Russian
Index 4 and language Chinese

----------------------

zip() function
--------------

Example Code

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

list(zip(developers, ids))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

--> Example with for looping 

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')

#
Name: Naomi
ID: 1
Name: Dario
ID: 2
Name: Jessica
ID: 3
Name: Tom
ID: 4

------------------------------------------------

What Are List Comprehensions and What Are Some Useful Functions to Work With Lists? (Working with Loops and Sequences)
-----------------------------------------------------------------------------------

Example Code -

even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

--> This example creates a new empty list called even_numbers and loops through a sequence of numbers between 0 and 20. Inside the loop, there's a condition that checks if the current number has a remainder of 0 when divided by 2. This is used to determine if the number is even. If the condition is True, then the current num is appended at the end of the even_numbers list. Finally, we print the even_numbers list to the console.

--> While this code works, there is a more concise way to write this that uses list comprehension instead. List comprehension allows you to create a new list in a single line by combining a loop and condition directly within square brackets. This makes the code shorter and often easier to read.

Example Code -

even_numbers = [num for num in range(21) if num % 2 == 0]
print (even_numbers)

-> For more understanding 

Example Code -

numbers = [1,2,3,4,5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]

# [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]

-----------------------------
filter() function
-----------------

Example Code -

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']

--> The filter() function is used to select elements from an iterable that meet a specific condition. The filter() function accepts a function and an iterable for its arguments. In this example, we are passing in an is_long_word function into the filter() function to check if the current word count is greater than 4. All words that have a character count greater than 4 are added into a new list and assigned to the long_words variable.

-----------------------------
map() function
--------------

Aside from the filter() function, there are a few more functions that are helpful when working with lists. Another function to be aware of is the map() function, which takes an iterable and applies a function to each of its elements. Here is an example of using the map() function to convert a list of temperatures from Celsius to Fahrenheit:

celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]

Another Example Code - 

# Convert a list of strings to integers
str_nums = ["1", "2", "3"]
int_nums = list(map(int, str_nums)) 
# Output: [1, 2, 3]

-----------------------------
positional argument
-------------------

numbers = [5, 10, 15, 20]
total = sum(numbers, 10) # positional argument
print(total) # 60


-----------------------------
keyword argument
----------------

numbers = [5, 10, 15, 20]
total = sum(numbers, start=10) # keyword argument
print(total) # 60

------------------------------------------------

What Are Lambda Functions and How Do They Work? (Working with Loops and Sequences)
-----------------------------------------------

When working with high order functions like map() and filter(), you can use an anonymous inline function. This is where lambda functions come in.

-> Here's what the square() function looks like when refactored into a lambda function:

lamda num: num ** 2

Using with filter()
-------------------

numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

Using with map()
----------------

--> When working with lambda functions it is important to be aware of best practices. For example, it is not a good practice to assign a lambda function to a variable like this:

numbers = [1, 2, 3, 4, 5]

square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]

--> This defeats the purpose of using anonymous functions. In this case, you should use a regular function, like this:

numbers = [1, 2, 3, 4, 5]

def square(num):
    return num ** 2

squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]



!!!Need to advoid like this using function!!!

result = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3)
print(result)  # 14

--> Using above instead, please use clear code and understandable 

def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x - 1
    else:
        return x**3 - x + 4

print(calculate_expression(3))  # 14


}


{

Date - 4/23/2026
================

-> I do extra project for today (Python Banking System)

Project: The Python Banking System
The Setup:
You will use a single nested list to represent your bank's database. Every time a new account is created, it gets added to this list.
Example: bank_db = [['Alex', 150.0], ['Jessica', 500.0]]

Here are your User Stories. You will need to write five different functions to make this work.

1. The Helper Function
Define a function named find_account_index(db, name).

It should use a for loop (and the enumerate() function you learned earlier) to search through the db list.

If it finds a nested list where the first item matches name, it should return that index number.

If the loop finishes and it never found the name, return -1. (You will use this helper function inside almost all your other functions so you don't have to rewrite your search loops!)

2. Creating Accounts
Define create_account(db, name, initial_deposit).

Validation: * If name is not a string, return 'Error: Name must be a string.'

If initial_deposit is less than 0, return 'Error: Deposit cannot be negative.'

Use your find_account_index function. If the account already exists (meaning it didn't return -1), return 'Error: Account already exists.'

Action: If all checks pass, append a new list containing the [name, initial_deposit] into the db. Return 'Success: Account created.'

3. Making Deposits
Define deposit(db, name, amount).

Validation: If the amount is less than or equal to 0, return an error. If the account does not exist, return an error.

Action: If valid, access the user's nested list using the index, add the amount to their balance, and return the new balance as a formatted string: 'Success: New balance is $X'.

4. Processing Transfers
Define transfer(db, sender_name, receiver_name, amount).

Validation: Check if BOTH accounts exist. Check if the amount is greater than 0.

Check if the sender actually has enough money in their balance to make the transfer. If they don't, return 'Error: Insufficient funds.'

Action: Deduct the money from the sender's balance, add it to the receiver's balance, and return 'Success: Transfer complete.'

5. Generating the Bank Report
Define print_bank_report(db).

Create a variable called total_bank_money set to 0.

Write a loop that goes through every account in the db.

Add each account's balance to the total_bank_money.

Format a massive multi-line string (using \n) that acts as a ledger, printing out every user, their balance, and the total money held by the bank at the bottom.

}



{

Date - 4/24/2026
================

-> I do extra project for today (Tech_Shop_inventory_System, Book Shop Inventory System, and Interactive Library System)


}


{

Date - 4/25/2026
================


What are Dictionaries, and How Do They Work? (Working with Dictionaries and Sets)
--------------------------------------------


In python, Dictionaries are build in data structures that store collections of key-value pairs.

They work very similarly to real dictionaries, where you search for a word to find its corresponding  meaning.

Syntax of a Python Dictionary - 

dictionary = {
    key1: value1,
    key2: value2
}


Example Code -

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

--> The dictionary is assigned to the pizza variable. It has four key-value pairs: name, price, calories_per_slice, and toppings.


---------------------------------------------
dict()
------

With above pizza example - 

pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

We can output with - dictionary[key]

Example - 

pizza['name']   #'Margherita Pizza'

To update -

pizza['name'] = 'Margherita'

so 

print(pizza['name']) # 'Margherita

------------------------------------------

.get()
------

dictionary.get(key, default)

Example code -

pizza.get('toppings', []) # ['mozzarella', 'basil']

------------------------------------------

.key() and .values()
--------------------

Example code -

pizza.keys()
# dict_keys(['name', 'price', 'calories_per_slice'])

pizza.values()
# dict_values(['Margherita Pizza', 8.9, 250])

------------------------------------------

.items()
--------

Example code -

pizza.items()
# dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])

------------------------------------------

.clear()
--------

Example code -

pizza.clear()

-----------------------------------------

.pop()
------

Example code -

pizza.pop('price', 10)
pizza.pop('total_price') # KeyError

------------------------------------------

.update()
---------

Example code -

pizza.update({ 'price': 15, 'total_time': 25 })


This is the new dictionary with the updated price and the new total_time. Notice how the price is now 15 and total_time is a new key-value pair:

{
    'name': 'Margherita Pizza', 
    'price': 15, 
    'calories_per_slice': 250, 
    'toppings': ['mozzarella', 'basil'], 
    'total_time': 25
}


---------------------------------------------------------------------

What Are Some Common Techniques to Loop Over a Dictionary? (Working with Dictionaries and Sets)
----------------------------------------------------------

You can loop over a dictionary if you need to access and process its key-value pairs. This is helpful for updating their values or applying some logic to them.

If we have this product dictionary -

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

------------------------------------

.values(), .keys(), .items()
----------------------------

for .values() -
    ---------

for price in products.values():
    print(price)

#990
 600
 250
 70

-------------------

for .keys() -
    --------

for product in products.keys():
    print(product)

//Or

for product in products:
    print(product)

#Laptop
 Smartphone
 Tablet
 Headphones

--------------------

for .items() -
    --------

for product in products.items():
    print(product)

#('Laptop', 990)
('Smartphone', 600)
('Tablet', 250)
('Headphones', 70)


Other Example - 

for product, price in products.items():
    print(product, price)

#Laptop 990
Smartphone 600
Tablet 250
Headphones 70

--------------------

Now that you know more about this, we can go back to our initial example. If we want to offer a 20% discount, we would multiply each price by 0.8 and reassign it as the value of that product key.

We could also round the result down if we want to work with integers:

Example Code -

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

#{
    'Laptop': 792, 
    'Smartphone': 480, 
    'Tablet': 200, 
    'Headphones': 56
}

----------------------

Using with enumerate()

for product in enumerate(products):
    print(product)

(0, 'Laptop')
(1, 'Smartphone')
(2, 'Tablet')
(3, 'Headphones')


--> If you need to, you can assign these values to separate loop variables. Here, we have two loop variables (index and product). This is what you will commonly see and use when you work with enumerate():


for index, product in enumerate(products):
    print(index, product)

------------

for price in enumerate(products.values()):
    print(price)

#(0, 990)
(1, 600)
(2, 250)
(3, 70)


for index, price in enumerate(products.values()):
    print(index, price)

# 0 990
1 600
2 250
3 70

-------------

for index, product in enumerate(products.items()):
    print(index, product)

# 0 ('Laptop', 990)
1 ('Smartphone', 600)
2 ('Tablet', 250)
3 ('Headphones', 70)

-> To customize the initial value of the count, you can pass a second argument to enumerate(). For example, here we are starting the count from 1:

for index, product in enumerate(products.items(), 1):
    print(index, product)

# 1 ('Laptop', 990)
2 ('Smartphone', 600)
3 ('Tablet', 250)
4 ('Headphones', 70)





}




{


Date - 4/26/2026
================

What are Sets, and How Do They Work? (Working with Dictionaries and Sets)
------------------------------------

Sets are one of Python's built-in data structures. One of the core characteristics of sets is that they don't store duplicate values. If you try to add a duplicate value to a set, only one of them will be stored.

Sets are mutable and unordered, which means that their elements are not stored in any specific order, so you cannot use indices or keys to access them. They can only contain values of immutable data types like numbers, strings, and tuples. And they support mathematical set operations, including union, intersection, difference, and symmetric difference.


Example Code -

my_set = {1, 2, 3, 4, 5} 

-------------------------

set() Function
--------------

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

One quirk of working with sets is that, if you ever need to define an empty set, you must use the set() function. If you just write empty curly braces, like {}, Python will automatically create a dictionary.

Example Code -

my_set.add(6)

#{1, 2, 3, 4, 5, 6}

-> If you try to add an element that is already in the set, only one will be kept. In this case, we already have the number 5 in the set:

my_set.add(5)

#{1, 2, 3, 4, 5, 6}

---------------------------

.remove() method
------------------

fruits = {"apple", "banana", "cherry"}

fruits.remove("banana") 

print(fruits)

#{'apple', 'cherry'}

-> If you have not remove item, you will get KeyError

---------------------------

.discard() method
-------------------

fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)

#{'apple', 'cherry'}

-> This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

--------------------------

.pop() method
-------------

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#{'apple', 'cherry'}

---------------------------

.clear() method
---------------

The .clear() method removes all the elements from the set:

my_set.clear()

---------------------------

Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#{True, 2, 'banana', 'cherry', 'apple'}

Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#{False, True, 'cherry', 'apple', 'banana'}

-----------------------------

len() Function 
--------------

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#3
------------------------------

subset() and superset()
-----------------------

A subset is a set whose elements are all contained within another set, while a superset is that "other" set which contains all the elements of the first set. They are two sides of the same coin: if A is a subset of B, then B is automatically a superset of A. 

Subset (⊆): Set A is a subset of B if every member of A is also in B.
Example: {1, 2} is a subset of {1, 2, 3}.

Superset (⊇): Set B is a superset of A if it includes everything in A.
Example: {1, 2, 3} is a superset of {1, 2}.

Proper Subset (⊂): A subset that is not equal to the original set.
Example: {1, 2} is a proper subset of {1, 2, 3}, but {1, 2, 3} is not a proper subset of itself. 


my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False

---------------------------------

isdisjoint()
------------

The .isdisjoint() method checks if two sets are disjoint, which means they don't have any elements in common. In this case, that's False because my_set and your_set do have common elements – 2, 3, and 4:

print(my_set.isdisjoint(your_set)) # False

--------------------------------

|, &, -, ^ 
-----------

The union operator | returns a new set with all the elements from both sets:

my_set | your_set # {1, 2, 3, 4, 5, 6}

The intersection operator & returns a new set with only the elements that the sets have in common:

my_set & your_set # {2, 3, 4}

The difference operator - returns a new set with the elements of the first set that are not in the other sets. In this example, the numbers 1 and 5 are in my_set but NOT in your_set:

my_set - your_set # {1, 5}

The symmetric difference operator ^ returns a new set with the elements that are either in the first or the second set, but not both. In this case, 1 and 5 are in my_set but not in your_set, so they are included. And the number 6 is in your_set but not in my_set, so it's included as well:

my_set ^ your_set # {1, 5, 6}

With Assignment Operator
------------------------

|= &= -= ^=

For example, the -= operator finds the difference between the sets and updates the first set with that result:

my_set -= your_set

After this, my_set will be updated to {1, 5}:

print(my_set) # {1, 5}

-----------------------------------

in operator
-----------

print(5 in my_set) #True

----------------------------------------------------------------

What is the Python Standard Library, and How Do you Import a Module? (Working with Modules)
--------------------------------------------------------------------------


}
{}

{}


{}


{}


{}


{}
