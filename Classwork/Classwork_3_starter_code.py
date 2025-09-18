# Name : Alice Smith ( your name here !)


# Part 1: Doubling the allowance . Starting from a penny per day , calculate
# how much allowance you ’d make on any given day , where the user is prompted
# for the day . Day 1: $0 .01 , Day 2: $0 .02 , Day 3: $0 .04 , Day 4: $0 .08 , etc .
start = 0.01
# prompt the user for a number to represent a day
day = ??
# calculate the total with a loop
for ???:
???  # put the body of the loop here



# Part 2: Tip Calculator. Write code which prompts the user for a sub-total
# and tip percentage, then display the final bill .
# Extra credit : handle both situations where the tip might be greater or less than
# one. For example. 10% could be 10.0 or 0.10.
# Remember to use the correct data type .
subtotal = ???
tip = ???
total = ?
print ( " Grand total : " , total )

# Part 3: Fibonacci calcuator . The Fibonacci sequence starts with 0 and 1 , and
# continues by adding the prior two digits . 0 and 1 become 1; 1 and 1 become 2;
#etc .
# The first few numbers in the sequence are : 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89.
# Write code to prompt the user for a number , and print the Fibonacci number at
# that position in the sequence .
num1 = 0

num2 = 1
count = ???
for ???:
    ???
    temp = num1 + num2
    num1 = num2
    num2 = temp

print ( " The number at position " , count , " is " , num2 )

# Part 4: Prime numbers . As the user for a number and test that it ’s a prime
# number . Do this by checking if the user ’s number is divisible by any of the
# numbers between 2 and the user ’s number minus one . As a shortcut , you may check
# numbers between 2 and the square root if the user ’s number .

import math # for sqrt ()

the_num = ???
is_prime = True

for _ in range (2 , math . sqrt ( the_num ) ) :
# Test that the number is prime , hint : use the % operator .

# Update ‘ is_prime ‘ appropriately .
# Exit early if isn’t prime .

if is_prime :
    print ( the_num , " is prime ! " )
else :
    print ( the_num , " is not prime . " )
