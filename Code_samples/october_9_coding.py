# in-class coding for Thursday, October 9

#  First the function definition
def reverse_word (word):
# now the code. DON’T FORGET TO INDENT!!

	reversed_word = ""
	for i in range(0, len(word)):
		reversed_word = reversed_word + word [-(i+1)]
#	return(reversed_word)
	word = reversed_word

if __name__ == '__main__':
    animals = ["cat", "Australian cattle dog", "duckbilled platypus", "ocelot", "zebra"]
    for critter in animals:
        print(reverse_word(critter))
        animal = reverse_word(critter)
        print(critter)
        print(animal)

