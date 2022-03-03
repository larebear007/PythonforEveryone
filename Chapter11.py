# 11.2 - Write a program to look for lines of the form: New Revision: 39772
# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and print out the average as an integer.

import re
name = input('Enter file: ')
handle = open(name)
nums = list()
for line in handle:
    x = re.findall('New Revision: ([0-9]+)', line)
    fx = float(x[0])
    nums.append(fx)
print(sum(nums)/len(nums))

# test comment

# 11.1- Write a simple program to simulate the operation of the
# grep command on Unix. Ask the user to enter a regular expression and
# count the number of lines that matched the regular expression:

import re
name = input('Enter file: ')
handle = open(name)
rx = input('Enter a regular expression to search for: ')
rx1 = '\'' + rx + '\''
print(rx1)
count = 0
for line in handle:
    if re.search(rx1, line):
        count = count + 1
print('The file', name,'has', count,'lines that match', rx)

quit()

# textbook follow along
import re
name = input('Enter file: ')
handle = open(name)
# print(handle)
for line in handle:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0: print(x)
quit()


import re
name = input('Enter file: ')
handle = open(name)
# print(handle)
for line in handle:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)
quit()


import re
name = input('Enter file: ')
handle = open(name)
# print(handle)
for line in handle:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)
quit()


import re
name = input('Enter file: ')
handle = open(name)
# print(handle)
for line in handle:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
quit()


# Regular Expressions 'Regex'

import re
x = 'My favorite 2 numbers are 4 and 44.'
y = re.findall('[0-9]+', x)
z = re.findall('[AEIOU]+', x)
print('Y=', y)
print('Z=', z)

xx = 'Find: something using the number: 5'
yy = re.findall('^F.+:', xx)
print(yy)

# old extraction method

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
spos = data.find(' ', atpos)
print(spos)
print('find method host:', data[atpos+1:spos])

words = data.split()
email = words[1]
host = email.split('@')
print('split method host:', host[1])

host1 = re.findall('@([^ ]*)', data)
print('new regX method 1 host:', host1[0])
# 0r
host2 = re.findall('From .*@([^ ]*)', data)
print('new regX method 2 host:', host2[0])

h = re.findall('\S+?@\S+', data)
print('h =', h)
