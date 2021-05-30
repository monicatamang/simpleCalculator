# Adding a custom exception by creating a class object with Exception as the argument, which is the base class for all defined exceptions
class CalculatorInputError(Exception):
    error_message = ""

    # Creating the constructor
    def __init__(self, message):
        self.error_message = message