# in-class cdoing from Tuesday, October 7
#
# showing how to use functions
import math

def area(n_sides, side_length):
    """
    Each function should have a comment block identifying:
    - the name of the function
    - a description of the function
    - what each parameter is
    - what the function returns
    """

    pi = math.pi
    answer = 0.25 *n_sides * side_length**2 * 1/math.tan(pi/n_sides)
    return answer

def print_message():
    print ("Welcome to my program")
    print("This program will calculate the area of any regular polygon")
    print("given the number of sides and the length of one side of the polygon")
    print ("Using the formula: area = (1/4)* number_of_sides * side_length**2* cotangent(pi/n_sides)")


def get_values():
    print_message()
    sides = int(input("Enter the number of sides of the polygon: "))
    length = float(input("Enter the length of the polygon: "))
    return sides, length

if __name__ == '__main__':

    s, l = get_values()
    a = area(s, l)
    print (a)

