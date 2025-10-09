# showing what happens when you use a list as a paramter

#  First the function definition
def reverse_list (l):

    new_list = l
    for i in range(len(l)):
        new_list.append(l[-i-1])


if __name__ == '__main__':
    animals = ["cat", "Australian cattle dog", "duckbilled platypus", "ocelot", "zebra"]
    reverse_list(animals)
    print(animals)