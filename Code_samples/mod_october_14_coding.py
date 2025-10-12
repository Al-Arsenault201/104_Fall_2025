#in-class coding for Tuesday, October 14

# an update on the original routine, showing how to use an else clause
# to add capability
#demonstrating how to use if, if-else and if-elif-else to implement
# conditional execution

def check_input(user_input):

    """
    Remeber that "user_input" is a string
    We will go through that string, character by character.
    In order for the input to be a valid integer:
    - The first character can be either a minus sign or a digit.
    A minus sign means it's a negative integer; a digit means it's non-negative
    - Every character *after* the first one must be a digit.

    This function will return a boolean variable, which will be True if the
    user entered a legal integer, and False if the input is anything else.
    """

    answer = True  # we will start by presuming that the user actually input an integer
    # we'll create a list variable containing all the legal digits. That
    # just makes coding easier later on.
    digits = ["0","1","2","3","4","5","6","7","8","9"]

    # now the actual checking
    if  not(user_input[0] in digits or user_input[0] == "-" ):
        answer = False
        return answer
    for i in range(1,len(user_input)):
        if not(user_input[i] in digits):
            answer = False
            return answer
    return answer

if __name__ == "__main__":
    print("This program takes an integer and returns the cube of that integer")
    value = input("Please enter an integer now")
    if check_input(value):
        print("The cube of that integer is ", int(value)**3)
    else:
        print ("I'm sorry, you did not enter an integer")
