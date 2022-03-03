# DICTIONARIES (hashmaps)

# 9.5 This program records the domain name (instead of the address) where the message
# was sent from instead of who the mail came from (i.e., the whole email address).
# At the end of the program, print out the contents of your dictionary.
fname = input('Enter a file: ')
try:
    fhand = open(fname)
    count = dict()
    for line in fhand:
        if not line.startswith('From '): continue
        words = line.split()
        email = words[1]
        host = email.split('@')
        host1 = host[1]
        count[host1] = count.get(host1, 0) + 1
    print(count)
except:
    print('File could not be opened or parsed:', fname)

quit()

# 9.4 Add code to the previous program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through the
# dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.
fname = input('Enter a file: ')
try:
    fhand = open(fname)
    count = dict()
    for line in fhand:
        if not line.startswith('From '): continue
        words = line.split()
        email = words[1]
        count[email] = count.get(email, 0) + 1
    # print(count)
    most_em = None
    most_val = None
    for email,v in count.items():
        if most_val is None or most_val < v:
            most_val = v
            most_em = email
    print('Most frequent email sender:', most_em, '(', most_val, 'emails)')

except:
    print('File could not be opened:', fname)

quit()


# 9.3 Write a program to read through a mail log, build a histogram using a dictionary
# to count how many messages have come from each email address, and print the dictionary.
fname = input('Enter a file: ')
try:
    fhand = open(fname)
    count = dict()
    for line in fhand:
        if not line.startswith('From '): continue
        words = line.split()
        email = words[1]
        count[email] = count.get(email, 0) + 1
    print(count)
except:
    print('File could not be opened:', fname)

quit()


# 9.2 Write a program that categorizes each mail message by which day of the week the
# commit was done. To do this look for lines that start with “From”, then look for the
# third word and keep a running count of each of the days of the week. At the end of the
# program print out the contents of your dictionary (order does not matter).
fname = input('Enter a file: ')
try:
    fhand = open(fname)
    count = dict()
    for line in fhand:
        if not line.startswith('From '): continue
        words = line.split()
        day = words[2]
        count[day] = count.get(day, 0) + 1
    print(count)
except:
    print('File could not be opened:', fname)

quit()

fname = input('Enter a file: ')
try:
    fhand = open(fname)
    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    print(counts)
except:
    print('File could not be opened:', fname)

quit()



# 8.1 exercise
name = input('Enter file name: ')
handle = open(name)
dictword = dict()
for line in handle:
    words = line.split()
    for word in words:
        dictword[word] = dictword.get(word, 'w')
print(len(dictword))
print('the' in dictword)

quit()


# Dictionaries - lecture playground

stuff = dict()
print(stuff.get('candy', -1))
val = stuff.values()
print(stuff)

quit()


name = input('Enter file name: ')
handle = open(name)
print(handle)
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
hfword = None
hfcount = None
for word,v in counts.items():
    if hfcount is None or hfcount < v:
        hfcount = v
        hfword = word
print('Highest frequency word:', hfword, ': seen', hfcount, 'times')


# print(counts1['chuck'])
# for key in counts1.items():
#     print(key, counts1[key])



quit()

# counts = dict()
# print('Enter a line: ')
# line = input('')
# words = line.split()
# print('Words:', words)
# print('Counting . . .')
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print('Counts:', counts)
# quit()