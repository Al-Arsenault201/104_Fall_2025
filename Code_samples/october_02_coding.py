#in-class coding for Thursday, October 2

fname = "/Users/alfredarsenault/Downloads/Fall_2025.csv"
with open(fname, "r") as infile:
    firstline = infile.readline()
#    print(firstline)
    secondline = infile.readline()
#    print(secondline)
    useful_data = infile.readlines()
#    for row in useful_data:
#       print(row)
    for row in range(len(useful_data)):
        useful_data[row] = useful_data[row].split(",")
#        print(useful_data[row])
        sum = 0
        useful_data[row][8] = int(useful_data[row][8])
        useful_data[row][8] = str(useful_data[row][8])
        for j in range(3,len(useful_data[row])):
            sum = sum + int(useful_data[row][j])
#        print(sum)
        useful_data[row].append(str(sum))
        print(useful_data[row][8])
#        print(useful_data[row])

with open("/Users/alfredarsenault/Downloads/Updated_Fall_2025.csv", "w") as outfile:
    outfile.write(firstline)
    outfile.write(secondline)
    for row in useful_data:
        outfile.write(",".join(row)+"\n")
