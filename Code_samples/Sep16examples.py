# ask the user to input a positive integer
#find the sum of all the numbers between 1 and the number that the user entered
sum = 0
print("Welcome to my program. Enter a positive integer ")
print(" and we will print out the sum off all the positive integers")
print("up to and including your number")
num = input("Please enter a positive integer: ")
for index in range(1,num+1,1):
    sum = sum + index
print("The answer is ", sum)
print("Thanks for playing. Isn't this cool?")
