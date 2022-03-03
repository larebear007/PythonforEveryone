#Rewrite the grade program from chapter 3 using a function called "computegrade"
# that takes a score as its parameter and returns a grade.

    #issue with return value for this function since it's not a formula
def computegrade(score):
    #score = float(input("\n\nPlease enter your exam score:"))
    if score < 0.0 or score > 1.0 :
        return "That won't work. Try a different score number.\n\n"
    elif score >= 0.9 :
        return "A\n\n"
    elif score >= 0.8 :
        return "B\n\n"
    elif score >= 0.7 :
        return "C\n\n"
    elif score >= 0.6 :
        return "D\n\n"
    elif score < 0.6 :
        return "F\n\n"


print(computegrade(0.8))


#Rewrite your pay computation with time-and-a-half for overtime
# and create a function called "computepay" which takes two paramenters (hours, rate)

def computepay(hours, rate):
    #hours = input("How many hours do you work each week?\n")
    #rate = input("How much do you get paid for each hour?\n")
    if float(hours) <= 40:
        grosspay = float(hours) * float(rate)
    elif float(hours) > 40:
        grosspay = float(rate) * (float(hours) + ((float(hours) -40)/2))
    #print("Your gross pay for each week is", grosspay)
    return grosspay

print("Your gross pay is: ",computepay(45, 10))



#random exploration

import random

f = random.randint(1, 10)
print(f)

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = random.choice(t)
print(x, "\n")

print(type(t))

for i in range(10):
    x = random.random()
    print(x)

