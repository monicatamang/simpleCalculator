def multiply_numbers(numbers_list):

    # Assigning the first number in the list as a variable. This is used to "initialize" the multiplication iteration
    product = numbers_list[0]

    # Creating a new list containing all the numbers from the original list excluding the first number. This is because numbers other than the first number is used in an iteration process where the first number is multiplied by the next number. The new product is calculated and the next number is multiplied from the product and so on
    new_numbers_list = numbers_list[1:]

    # Iterating through the new list created
    for number in new_numbers_list:

        # In general, the result is calculated by multiplying two numbers to get the product and then multiplying the product with the next number in the new list
        result = product * number

        # Once the new result is calculated, it is set as the new product and the iteration process is repeated
        product = result

    # Returning the value
    return result