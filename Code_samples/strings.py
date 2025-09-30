#coding explaining string operations

string1 = "UMBC"
string2 = "University of Maryland Baltimore County"
string3 = "the quick brown fox jumped over the lazy dog"

#calculating the length of a string
print(len(string2))

#printing out each character in a string, one at a time
for i in range(0,len(string2)):
    print(string2[i])

#convert to uppercase
print(string3.upper())

#concatenating strings to form a new string
string4 = string2 + " also known as " + string1
print(string4)

#string slicing - printing out only some of the letters in a string
print(string2[0:22])

#another way of accomplishing the same thing
print(string2[:22])

#attempting to modify a single character in a string
#note - this will fail.
#you can't do this because strings are immutable
#string2[21] = "e"

#if you want to do that you have to create a new version of string2:
string2 = string2[:21] + "e" + string2[22:]
print(string2)

#splitting a string
print(string2.split())

#splitting a string on some character other than whitespace
print(string2.split('a'))

#stripping leading and trailing blank spaces from a string
string5 = "   UMBC   "
print(string5.strip())

#you can't change an individual character in a string
#but you can reference one
print(string1[0])  #note the square brackets

print(string1[1])

#you can start referencing at the end by using negative indices
print(string1[-1])
print(string1[-3])
