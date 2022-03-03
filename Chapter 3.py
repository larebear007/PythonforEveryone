#Rewrite your pay program using try and except so that your program handles non-numeric
# input gracefully by printing a message and exiting the program. ***

try:
    hours = float(input("How many hours do you work each week?\n"))
    rate = float(input("How much do you get paid for each hour?\n"))
    if hours <= 40:
        grosspay = hours * rate
    elif hours > 40:
        grosspay = float(rate) * (float(hours) + ((float(hours) -40)/2))
    print("Your gross pay for each week is", grosspay)
except:
    print("Please enter a number for your hours and pay")


#Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message.
# If the score is in range, print a grade of A-F.

score = float(input("Please enter your exam score:"))

if score < 0.0 or score > 1.0 :
    print("That won't work. Try a different score number.\n\n")
elif score >= 0.9:
    print("A\n\n")
elif score >= 0.8 :
    print("B\n\n")
elif score >= 0.7 :
    print("C\n\n")
elif score >= 0.6 :
    print("D\n\n")
elif score < 0.6 :
    print("F\n\n")







#Rewrite your pay computation to give your employee 1.5 times the hourly rate for hours worked
#above 40 hours

hours = input("How many hours do you work each week?\n")
rate = input("How much do you get paid for each hour?\n")
if float(hours) <= 40:
    grosspay = float(hours) * float(rate)
elif float(hours) > 40:
    grosspay = float(rate) * (float(hours) + ((float(hours) -40)/2))
print("Your gross pay for each week is", grosspay)
