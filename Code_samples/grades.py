# a program illustrating what happens when multiple boolean expressions are True:

if __name__ == "__main__":
    grade = 95
    if grade >90:
        print ("You get an A")
    elif grade > 80:
        print("You get a B")
    elif grade > 70:
        print("You get a C")
    elif grade > 60:
        print ("You get a D")
    else:
        print ("Sorry, you get an F")