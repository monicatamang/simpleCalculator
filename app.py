from exception import CalculatorInputError
import re
import addition
import subtraction
import multiplication
import division

# Creating a function that searches for invalid characters from the user's input
def check_invalid_chars(user_input):

    # Using the regular expression library in python, the compile and search methods are used to store and find all characters that are not digits, i.e., any number between 0 and 9 
    invalid_chars = re.compile(r'\D').search(user_input)

    # If any characters, other than digits (0 - 9), are found in the user's input, it will return "true"
    if(invalid_chars):
        return True

# Printing the user's options
print("Welcome to the simple calculator, please select from the following options:")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

# Creating a try block to catch and handle runtime errors associated with the selection menu
try:
    # Prompting the user to make a selection from the four options in a "string" format
    user_selection_string = input("Please enter your selection: ")

    # Calling the function to check if the user's input contains invalid characters
    is_user_selection_invalid = check_invalid_chars(user_selection_string)

    # If the user's input contains invalid characters, raise the CalculatorInputError exception and create the object instance with the following error message
    if(is_user_selection_invalid == True):
        raise CalculatorInputError(f"CalculatorInputError: '{user_selection_string}' Invalid character(s). Expected a numerical value.")
except CalculatorInputError as select_error:
    # Print the error message to the user in the terminal
    print(select_error.error_message)

    # Prompt the user to make their selection again
    user_selection_string = input("Please enter your selection: ")

# Converting the user's input into an integer
user_selection_number = int(user_selection_string)

# Spliting up the user's input into separate strings which returns a list containing the substrings
user_input_strings = input("Please enter the numbers you wish to calculate and separate each number with a space. You must enter at least two numbers: ").split()

# Creating a try block to catch and handle runtime errors associated with inputting the numbers used in the math operations
try:
    # For every character in the user's input, check whether it has characters other than digits
    for user_input_char in user_input_strings:
        is_user_chars_invalid = check_invalid_chars(user_input_char)

        # If invalid characters are found, raise an exception and create an object instance with the following error message
        if(is_user_chars_invalid):
            raise CalculatorInputError(f"CalculatorInputError: '{user_input_char}' Invalid character(s). Expected numerical values.")
except CalculatorInputError as calc_error:
    # Printing the error message to the user in the terminal
    print(calc_error.error_message)

    # Prompt the user enter two or more numbers again
    user_input_strings = input("Please enter the numbers you wish to calculate and separate each number with a space. You must enter at least two numbers: ").split()

# Definition: map() is used to execute a specific function for each item in a list without explicitly using a loop which returns a map object
# Converting each string in the list into a float data type then converting the map object into a list so that it can be used to calculate certain values based on the math operation the user has selected
user_input_numbers = list(map(float, user_input_strings))

# Creating a conditional that will perform a specific math operation based on the user's selection
if(user_selection_number == 1):
    addition_result = addition.add_numbers(user_input_numbers)
    print(f"Your result: {addition_result}")
elif(user_selection_number == 2):
    subtraction_result = subtraction.subtract_numbers(user_input_numbers)
    print(f"Your result: {subtraction_result}")
elif(user_selection_number == 3):
    multiplication_result = multiplication.multiply_numbers(user_input_numbers)
    print(f"Your result: {multiplication_result}")
elif(user_selection_number == 4):
    division_result = division.divide_numbers(user_input_numbers)
    print(f"Your result: {division_result}")

# ORIGINAL ASSIGNMENT: TAKING TWO USER INPUTS

# Creating two user inputs
# first_number = float(input("Please enter your first number: "))
# second_number = float(input("Please enter your second number: "))

# Creating a conditional that will perform a specific math operation based on the user's selection
# if(selection == 1):
#     addition_result = addition.add_numbers(first_number, second_number)
#     print(f"Your result: {addition_result}")
# elif(selection == 2):
#     subtraction_result = subtraction.subtract_numbers(first_number, second_number)
#     print(f"Your result: {subtraction_result}")
# elif(selection == 3):
#     multiplication_result = multiplication.multiply_numbers(first_number, second_number)
#     print(f"Your result: {multiplication_result}")
# elif(selection == 4):
#     division_result = division.divide_numbers(first_number, second_number)
#     print(f"Your result: {division_result}")