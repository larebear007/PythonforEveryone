# 6.6 - Play with string methods, especially .strip and .replace
word1 = 'Hallelujah'
word2 = 'hallelujah'
word3 = 'halleluyah'

if word1.lower() == word2.lower():
    print('nice')
elif word1.lower() != word2.lower():
    print('oopsie poopsie. 1 & 2 don\'t match')
if word2.lower() == word3.lower():
    print('nice')
elif word2.lower() != word3.lower():
    print('oopsie poopsie. 2 & 3 don\'t match')
quit()



str1 = 'i like to '
str2 = 'eat eat eat apples and bananas'
str3 = str2.replace('a','o')
str4 = str1 + str3
print(str4)
quit()


data = '       hey     '
data1 = '..$.. fj. hey$.there$.! ..$..'
print(data.strip())
print(data1.strip('. $fj'))
quit()



# 6.5 - Use find and string slicing to extract the portion of code afte the ':'
# and then use the float function to convert  the extracted string into a floating point number

data = 'X-DSPAM-Confidence:0.8475'
colpos = data.find(':')
num = float(data[colpos+1:])
print(num)
print(type(num))
quit()



data = 'Email from larencozart@gmail.com on Saturday January 4, 2022'
atpos = data.find('@')
print(atpos)
spos = data.find(' ',atpos)
print(spos)
host = data[atpos+1:spos]
print(host)
quit()




# 6.4 use the preset method "count" on the word 'banana' to see how many a's there are

word = 'banana'
print(word.count('a'[:]))
quit()


# 6.3 Encapsulate the letter count program into a function named "count",
# and generalize it so that it accepts the string and letter as the argument.
# don't know how to generalize parameters
def count(word, letter):
    count = 0
    for current_letter in word:
        if current_letter == letter:
            count = count + 1
    print(count)


count('mississippi', 's')
quit()

# 6.1 - Write a while loop that starts at the last character in the string and works
# its way backwards to the first character, printing each letter on a separate line, backwards.
me = 'laren'
x = len(me) - 1
while x >= 0:
    print(me[x])
    x = x - 1
quit()

# video: playing with strings and indexes
x = 'Hello Brian'
print(x.replace('Brian', 'Laren'))

quit()

x = input("Tell me your name: ")
lower_x = x.lower()
print(lower_x)
quit()

word = 'Laren Cozart'
print(word[:5])
print(word[6:])
print(word[:])
count = 0
if 'a' in word:
    count = count + 1
    print('True', count)
else:
    print('False')
quit()

count = 0
word = 'banana'
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

fruit = "banana"
count = -1
for letter in fruit:
    count = count + 1
    print(count, letter)

fruit = 'banana'
x = 0
while x < len(fruit):
    i = fruit[x]
    print(x, i, '\n')
    x = x + 1

fruit = "banana"
print(len(fruit))
