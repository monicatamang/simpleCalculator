def subtract_numbers(numbers_list):

    # Assigning the first number in the list as a variable. This is used to "initialize" the subtraction iteration
    difference = numbers_list[0]

    # Creating a new list containing all the numbers from the original list excluding the first number. This is because numbers other than the first number is used in an iteration process where the next number is subtracted by the first number. The new difference is calculated and the next number is subtracted from the difference and so on
    new_numbers_list = numbers_list[1:]
    
    # Iterating through the new list created
    for number in new_numbers_list:

        # In general, the result is calculated by subtracting two numbers to get the difference and then subtracting the difference from the next number in the new list
        result = difference - number

        # Once the new result is calculated, it is set as the new difference value and the iteration process is repeated
        difference = result

    # Returning the value
    return result

    # Further explanation

    # Original List: [100, 5, 22, 87, 60]

    # Initially setting the difference as the first number, difference = 100

    # New List: [5, 22, 87, 60]

    # Starting the iteration process, for number in new_numbers_list:
    # result = 100 - 5 = 95
    # difference = result = 95

    # Second iteration
    # result = 95 - 22 = 73
    # difference = result = 73

    # This process is repeated until the last number in the list is subtracted by the final difference

    # Note: I originally used the numbers_list to go through the iteration process but was running into issues, specifically when calculating the result because for the first number it was calculating, result = numbers_list[0] - numbers_list[0] = 0 which would return an incorrect value to the user