"""
This program reads a text file (.txt). It breaks the file up into a list of words.  Then it counts the frequency
of each word. It allows the user to print out the word and count of the X most common words, where X is an integer chosen by the user

"""
def getwordlist(filename):

    #first read in the file contents as a single string
    with open(filename, "r") as f:
        data = f.read()

        # we have the words as a single string. We are going to remove all punctuation, because
        # that could mess up our word counts

        #print(data[1:100])

        for ch in '!"#$%&()*+/,.:;<=>?@[]{}||_-|':
            data = data.replace(ch, '')
        #print(data[1:100])
        list_of_words = data.split()
        return list_of_words

def create_dictionary(list_of_words):
    dictionary = {}
    for word in list_of_words:
        dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary

def organize (d):
    items = list(d.items())
    items.sort()
    items.sort(key=byFrequency, reverse=True)
    return items

def byFrequency(list_of_words):
    return list_of_words[1]

if __name__ == '__main__':
    fname = input('Enter file name: ')
    contents = getwordlist(fname)
    #contents now contains the list of words in the file
    #create a dictionary that contains a list of the words in the dictionary and the
    #number of times each word has appeared
    word_count = create_dictionary(contents)
    #now create a list of the word, count pairs in the dictionary, and put them in order
    #from most common to least common
    common_list = organize(word_count)

    #print 10 items
    for i in range(10):
        print(common_list[i])




