# 5.2 - Write another program that prompts for a list of numbers,
# and at the end prints out both the max and min.
maxx = None
minn = None
while True:
    val = input('Enter a number: ')
    if val == 'done':
        break
    try:
        fval = float(val)
        if maxx is None:
            maxx = fval
        elif fval > maxx:
            maxx = fval
        if minn is None:
            minn = fval
        elif fval < minn:
            minn = fval
    except:
        print('Invalid data')
        continue
print("Max: ",maxx,"\nMin:", minn)






# max = None
#
# while True:
#     try:
#         x = input("Enter a number: ")
#         max_x = int(x)
#         if max is None:
#            max = max_x
#         elif x > max:
#            max = max_x
#     except:
#         print("No...")
#         continue
# print("Max: ", max)



#5.1- Wrtie a program that reads numbers repeatedly until the user enters "done".
# Once done, print out a count, total and average of numbers.
# If the user enters something besides a number, print an error message, and skip to the next number input.

count = 0
intSum = 0
average = 0
while True:
    x = input("Enter an integer: ")
    if x == "done":
        break
    else:
        try:
            intX = int(x)
            count = count + 1
            intSum = intSum + intX
            average = intSum/count
        except:
            print("No...")
            continue

print("Count: ", count)
print("Sum: ", intSum)
print("Average: ", average)



#loop exploration
list = [9, 41, 12, 3, 74, 15]
print(sum(list))
print(len(list))
print(min(list))
print(max(list))


while True:
    try:
        hours = float(input("How many hours do you work each week?\n"))
        rate = float(input("How much do you get paid for each hour?\n"))
        if hours <= 40:
            grosspay = hours * rate
        elif hours > 40:
            grosspay = float(rate) * (float(hours) + ((float(hours) -40)/2))
        print("Your gross pay for each week is", grosspay)
        break
    except:
        print("Please enter a number for your hours and pay")
        continue


print("\n\n")


# ANOTHER WAY TO DO THE SMALLEST_SO_FAR: combine both if statements with an or since assignment statement
# that follows is the same after

# smallest_so_far = None
# for i in [9, 41, 12, 3, 74, 15]:
#     if smallest_so_far is None or i < smallest_so_far:
#         smallest_so_far = i
#     print(smallest_so_far, i)
# print("The smallest number was:", smallest_so_far)


smallest_so_far = None
for i in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None:
        smallest_so_far = i
    elif i < smallest_so_far:
        smallest_so_far = i
    print(smallest_so_far, i)
print("The smallest number was:", smallest_so_far)

print("\n\n")

count = 0
found = False
for i in [9, 41, 12, 3, 4, 6, 74, 89, 90, 15]:
    count = count + 1
    if i == 3:
        found = True
        break
print(found, i, "is in the", count,"position")


runningtotal = 0
for i in [9, 41, 12, 3, 74, 15]:
    runningtotal = runningtotal + i
    print(i,"+")
print("=", runningtotal)
print("The average was:", runningtotal/6)

largest_so_far = -1
for i in [9, 41, 12, 3, 74, 15]:
    if i > largest_so_far:
        largest_so_far = i
    print(i, largest_so_far)


while True:
    line = input("- ")
    if line == "seriously stop" :
            break
    print(line)
print("Okay")



n = 5
while n > 0 :
    print(n)
    n = n - 1
print("All Done!")
print(n)