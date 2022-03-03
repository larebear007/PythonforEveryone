#playing with files

# 7.1 - 7. 3 exercises
fname = input('Enter file name: ')
try:
    if fname == 'na na na boo boo':
        print('Nice try, punk!')
    fhand = open(fname, 'r')
    print(fhand)
except:
    print('Please try entering an existing file name.')
    quit()

quit()

count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        nums = float(line[20:26])
        total = total + nums
        spamavg = total/count
# print('Spam confidences:', count)
# print('Sum of spam confidences:', total)
print('Average spam confidence:', spamavg)
quit()

fname = input('Enter file name: ')
try:
    fhand = open(fname,'w')
    print(fhand)
    line1 = 'Hello, I am typing in a file now!\n'
    fhand.write(line1)
    line2 = 'Now, I will try to close this thing, and check it!'
    fhand.write(line2)
    fhand.close()
except:
    print('Please try entering an existing file name.')
    quit()


quit()


count = 0
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    # print(line)
    count = count + 1
print('Line count:',count)

