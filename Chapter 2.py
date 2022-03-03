#Write a program which prompts the use to enter a Celcius temperature, convert to Fahrenheit,
#and print the converted temperature

celsius = input("What is the temperature in degrees Celcius today?")
fahrenheit = float(celsius) * 1.8 + 32
print("Today's temperature in degrees Fahrenheit is ",fahrenheit)

#Write a program that uses input to prompt a user for their name and then welcomes them

name = input("Hello! What is your name?\n")
print("Nice to meet you,",name,"!\n\n")

#Write a program to prompt the user their hours and rate per hour to compute their gross pay

hours = input("How many hours do you work each day?\n")
rate = input("How much do you get paid for each hour?\n")
grosspay = float(rate) * float(hours)
print("Your gross pay for each day is", grosspay)
