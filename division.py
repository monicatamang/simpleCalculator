def divide_numbers(numbers_list):

    # Assigning the first number in the list as a variable. This is used to "initialize" the division iteration
    quotient = numbers_list[0]

    # Creating a new list containing all the numbers from the original list excluding the first number. This is because numbers other than the first number is used in an iteration process where the first number is divided by the next number. The new quotient is calculated and the next number is divided from the quotient and so on
    new_numbers_list = numbers_list[1:]

    # Iterating through the new list created
    for number in new_numbers_list:

        # In general, the result is calculated by dividing two numbers to get the quotient and then dividing the quotient with the next number in the new list
        result = quotient / number

        # Once the new result is calculated, it is set as the new quotient value and the iteration process is repeated
        quotient = result
    
    # Returning the value
    return result