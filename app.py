import addition
import subtraction
import multiplication
import division

# Printing user options
print("Welcome to the simple calculator, please select from the following options:")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

# Printing user prompt to select an option
selection = int(input("Please enter your selection: "))

# Creating two user inputs
first_number = float(input("Please enter your first number: "))
second_number = float(input("Please enter your second number: "))

# Creating a conditional that will perform a specific math operation based on the user's selection
if(selection == 1):
    addition_result = addition.add_numbers(first_number, second_number)
    print(f"Your result: {addition_result}")
elif(selection == 2):
    subtraction_result = subtraction.subtract_numbers(first_number, second_number)
    print(f"Your result: {subtraction_result}")
elif(selection == 3):
    multiplication_result = multiplication.multiply_numbers(first_number, second_number)
    print(f"Your result: {multiplication_result}")
elif(selection == 4):
    division_result = division.divide_numbers(first_number, second_number)
    print(f"Your result: {division_result}")