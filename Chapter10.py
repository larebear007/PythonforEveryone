# Write a program that reads a file and prints the letters in decreasing order of
# frequency. Your program should convert all the input to lower case and only count the letters
# a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters
# a-z. Find text samples from several different languages and see how letter frequency varies between
# languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

try:
    name = input('Enter file name: ')
    handle = open(name)
    print(handle)
    dcount = dict()
    import string
    for line in handle:
        line = line.translate(line.maketrans('' ,'', string.punctuation))
        line = line.lower()
        words = line.split()
        letters = list(''.join(words))
    # print(letters)
        for letter in letters:
            dcount[letter] = dcount.get(letter, 0) + 1
    list1 = sorted([(v, k) for k, v in dcount.items()], reverse=True)
    count = 0
    for v, k in list1:
        count += 1
        print(count,':', k, v)

except:
    print('File could not be opened or parsed:', name)
quit()



# 10.2 This program counts the distribution of the hour of the day for each of the
# messages. You can pull the hour from the “From” line by finding the time string and then splitting
# that string into parts using the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour as shown below.
try:
    name = input('Enter file name: ')
    handle = open(name)
    print(handle)
    count = 0
    dct = dict()
    for line in handle:
        if not line.startswith('From '): continue
        words = line.split()
        # print(words)
        time = words[5]
        hour = time[0:2]
        dct[hour] = dct.get(hour, 0) + 1
    for k, v in sorted(dct.items()):
        print(k, v)
    # print(dct)
except:
    print('File could not be opened or parsed:', name)

quit()



# 10.1 Revise a previous program as follows: Read and parse the “From” lines and pull out
# the addresses from the line. Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of
# (count, email) tuples from the dictionary. Then sort the list in reverse order and print out
# the person who has the most commits.

try:
    fname = input('Enter file name: ')
    fhand = open(fname)
    ecount = dict()
    for line in fhand:
        if not line.startswith('From '): continue
        words = line.split()
        email = words[1]
        ecount[email] = ecount.get(email, 0) + 1
    # print(ecount)
    # quit()
    # elist = list(ecount.item())
    # print(elist)
    # quit()
    elist = sorted([(v, k) for k, v in ecount.items()], reverse=True)
    for v, k in elist[0:1]:
        print(k, v)

except:
    print('File could not be openend or parsed:', fname)

quit()




# Tuples - Playground
stuff = {'a': 1, 'b': 2, 'c': 3}
l_stuff = stuff.items()
print(l_stuff)
quit()

address = 'larencozart@gmail.com'
user, domain = address.split('@')
print(address)
print(user)
print(domain)

user, domain = domain, user
print(domain, user)

# A second way of writing the same code using "LIST COMPREHENSION"
fname = input('Enter file name: ')
try:
    fhand = open(fname)
    wordcount = dict()
    # print(fhand)
    for line in fhand:
        words = line.split()
        for word in words:
            wordcount[word] = wordcount.get(word, 0) + 1
    # print(wordcount)
    print(sorted([ (v,k) for k, v in wordcount.items()], reverse=True))


except:
    print('File could not be open or parsed:', fname)

quit()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
    wordcount = dict()
    # print(fhand)
    for line in fhand:
        words = line.split()
        for word in words:
            wordcount[word] = wordcount.get(word, 0) + 1
    # print(wordcount)
    lst = list()
    for key, val in wordcount.items():
        # print(k, v)
        newtup = (val, key)
        lst.append(newtup)
    print(lst)
    lst = sorted(lst, reverse=True)
    count = 0
    for v, k in lst[:10]:
        count += 1
        print(count, ':', k, v)

except:
    print('File could not be open or parsed:', fname)

quit()