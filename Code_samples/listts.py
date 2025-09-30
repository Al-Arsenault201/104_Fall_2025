#coding using lists

counties = ["Allegany", "Anne Arundel","Baltimore", "Baltimore City", "Calvert", "Carroll", "Caroline", "Cecil", "Charles", "Dorchester",
"Frederick", "Garrett", "Harford", "Howard", "Kent", "Montgomery", "Prince George's", "Queen Anne's", "Somerset", "St. Mary's",

"Talbot", "Washington", "Wicomico", "Worcester"]

#check to see if we got them all
print(len(counties))

#49 ofthe 50 US states
# I left out Maryland - that was intentional
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
          "Hawaii","Idaho", "Indiana", "Illinois", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
"Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
          "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
          "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin",
          "Wyoming"]

#check to see how many we have
print(len(states))

#Use append to add Maryland to the end of the list
states.append("Maryland")
print(states)

# but they're not in alphabetical order. We need to remove Maryland, and put
#it in the right place
states.remove("Maryland")
print(len(states))

#now, use insett to put Maryland where it belongs. It's in place
#19
states.insert(19,"Maryland")
print(states)

#note that we can change lists on the fly like this - unlike strings.
#That's because list are mutable - they can be changed in place

#slicing lists
print(states[:10])
print("The next states are: ", states[11:20])

#picking out individual states using a different kind of for loop
for state in states:
    if state[0] == "M":
        print(state)


