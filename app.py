import addition
import subtraction
import multiplication
import division

# Printing the user's options
print("Welcome to the simple calculator, please select from the following options:")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

# Prompting the user to select an option
selection = int(input("Please enter your selection: "))

# Spliting up the user's input into separate strings which returns a list containing the substrings
user_input_strings = input("Please enter the numbers you wish to calculate and separate each number with a space. You must enter at least two numbers: ").split()

# Definition: Map() is used to execute a specific function for each item in a list without explicitly using a loop which returns a map object.
# Converting each string in the list into a float data type then converting the map object into a list so that it can be used to calculate certain values based on the math operation the user has selected
user_input_numbers = list(map(float, user_input_strings))

# Creating a conditional that will perform a specific math operation based on the user's selection
if(selection == 1):
    addition_result = addition.add_numbers(user_input_numbers)
    print(f"Your result: {addition_result}")
elif(selection == 2):
    subtraction_result = subtraction.subtract_numbers(user_input_numbers)
    print(f"Your result: {subtraction_result}")
elif(selection == 3):
    multiplication_result = multiplication.multiply_numbers(user_input_numbers)
    print(f"Your result: {multiplication_result}")
elif(selection == 4):
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