# LISTS
# *range function

# 8.6 Rewrite the program that prompts the user for a list of numbers and prints out the maximum
# and minimum of the numbers at the end when the user enters “done”. Write the program to store the
# numbers the user enters in a list and use the max() and min() functions to
# compute the maximum and minimum numbers after the loop completes.

nums = list()
while True:
    try:
        val = input('Enter a number: ')
        if val == 'done':
            break
        fval = float(val)
        nums.append(fval)
    except:
        print('No...')
print('Min value:', min(nums), 'Max value:', max(nums))
nums.sort()
print(nums)
quit()


# 8.5 Write a program to read through the mail box data and when you find
# line that starts with “From”, you will split the line into words using the
# split function. We are interested in who sent the message, which is the
# second word on the From line. You will parse the From line and print out the second word for each
# From line, then you will also count the number of From (not From:) lines and print out a count at the end.

fname = input('Enter file name: ')
fhand = open(fname)
print(fhand)
count = 0
for line in fhand:
    if line.startswith('From '):
        count = count + 1
        words = line.split()
        print(words[1])
print('Number of From lines:', count)


quit()


# 8.4 Find all unique words in a file:
# Create a list of unique words, which will contain the final result. Write
# a program to open the file romeo.txt and read it line by line. For each line, split the line into a list
# of words using the split function. For each word, check to see if the word is already in the list of unique
# words. If the word is not in the list of unique words, add it to the list. When the program completes,
# sort and print the list of unique words in alphabetical order.


uwords = ['but', 'soft', 'what']

fname = input('Enter file name: ')
fhand = open(fname)
print(fhand)
for line in fhand:
    words = line.split()
    for word in words:
        lword = word.lower()
        if lword not in uwords:
            uwords.append(lword)
uwords.sort()
print(uwords)
print(len(uwords))



quit()




# 8.2 and 8.3 looking for unguarded code - modify without 2 if statements-> instead one if and an 'or'

fhand = open('mbox.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From': continue
    print(words[2])
quit()


# 8.1 - Write a function called 'chop' that takes a list, and modifies it,
# removing the first and last elements, and returns None.
# Then write a function called 'middle' that takes a list and makes a new list
# that contains all but the first and last elements.

def middle(x):
    x2 = x[1:-1]
    return x2
quit()


list3 = ['l', 'a', 'r', 'y', 'n']
xyz = middle(list3)
print(xyz)

def chop(x):
    del x[0]
    del x[-1]
    print(x)
    quit()


list1 = ['s', 'o', 'p', 'p', 'y']
list2 = chop(list1)
print(list2)
quit()


# lecture/text playground - lists

a = ['banana']
b = a
if a is b:
    print('True')
    print(a)
    print(b)
else:
    print('False')
quit()


str = 'i am writing a string'
x = str.split()
print(x)

delimiter = '+'
print(delimiter.join(x))
quit()


name = 'laren'
letters = list(name)
print(letters[0])
quit()


stringy = [0, 2, 4, 6, 8, 10]
print(stringy)
quit()

story = ['Once upon a time there was a computer.', '']
one = ['There was also a girl,', 'a charger,', 'and a dream!']
story.extend(one)
print(story)

story = ['Once upon a time there was a computer.', '']
one = ['There was also a girl,', 'a charger,', 'and a dream!']
story.append(one)
print(story)
quit()

name = ['laren', 'brian']
pet = ['cat', 'cat2']
mult = (name + pet)* 2
print(mult)
quit()


#splitting
fname = input('Enter file name: ')
try:
    if fname == 'na na na boo boo':
        print('Nice try, punk!')
    fhand = open(fname, 'r')
    print(fhand)
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From '): continue
        words = line.split()
        email = words[1]
        provider = email.split('@')
        # print(provider)
        p2 = provider[1]
        print(p2)
except:
    print('Please try entering an existing file name.')

quit()


phrase = 'I am learning how to code.'
sphrase = phrase.split()
print(len(sphrase))
print(sphrase)
for word in sphrase:
    print(word)
quit()


# different way to do a counter: .append or loop
# .append
numlist = list()
while True:
    x = input("Enter an integer: ")
    if x == "done":
        break
    else:
        try:
            fx = float(x)
            numlist.append(fx)
        except:
            print("No...")
            continue
avg = sum(numlist)/ len(numlist)
print('Average: ', avg)
quit()


# loop way
count = 0
total = 0
while True:
    x = input("Enter an integer: ")
    if x == "done":
        break
    else:
        try:
            fx = float(x)
            count = count + 1
            total = total + fx
            average = total / count
        except:
            print("No...")
            continue

print("Count: ", count)
print("Sum: ", total)
print("Average: ", average)
quit()

test = [2, 4, 'cat', 1, 'alpha', 5, 'bravo', 3, 0]
strtest = str(test)
print(strtest.sort())
quit()

stuff = list()
stuff.append('books')
print(stuff)
stuff.append('movies')
print(stuff)
stuff.append('and more!')
print(stuff)

quit()

friends = ['Josephy', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year,', friend)
# way to create a counted loop over a list without initializing + adding extra increment code
friends2 = ['Amayra', 'Jake', 'Lorcan']
for i in range(len(friends2)):
    friend2 = friends2[i]
    print(i, 'Happy New Year,', friend2)
quit()

# list1 = [0, 1, 2, 3, 4, 5]
# print(list1)
# list1[3] = 3000
# print(list1)
list2 = ['laren and brian have been married for', '4', 'years']
list2[1] = 3
print(list2)
print(len(list2))
