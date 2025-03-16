# first importing libraries
from math import *

# taking a string and number for different function operations
char_1 = "Harigovind"
char_2 = 27.8
# some of the common functions are used here
print(round(char_2))                                   #to round the number
print(abs(char_2))                                     #to take absolute value
print(char_1.upper())                                  #to convert to upper case
print(char_1.isupper())                                #to check if the string is in upper case (boolean function)
print(char_1.lower().islower())                        #combination of above two for lower case (islower is boolean function)
print(char_1.islower())
print(round(pow(char_2, 2)))                     #to take power of a number to another number
print(len(char_1))                                     #to find length of string
print(char_1 + " is " + str(char_2) + " years old.")   #to print combination of numbers and strings, we can also use print f
print(char_1[3])                                       #to print the char at the mentioned index
print(char_1.index("i"))                               #to print position of index of the mentioned character, 1st occuring position will be displayed

print(floor(char_2))                                   #print after rounding off value to lower limit
print(ceil(char_2))                                    #print after rounding off value to upper limit

print(sqrt(36))                                        #print square root of value
print(type(char_1))                                    #type command prints type of variable
print(type(char_2))
print(type(int(char_2)))                               #variable type is converted and then printed
print(type(str(char_2)))

print(100%10)                                          #modulus operator gives remainder value
print(100%9)                                           #should give 1

#input function and data types

name = input("Enter your family name \n ")             #inputing values
height = input("Enter your height in cm \n")           #by default python intakes all inputs as strings, so here,height will be a string, not number
print("Hello " + char_1 + " " + name + "!")            #concatenation of string
print(f"Your age is {round( char_2)}")                 #printing both string and number using printf
print("Your height is " + height + "cm")               #basically the above print statement converts string into int using round(), this is another option without rounding
num1 = input("Enter a number\n")
num2 = input("Enter another number\n")
Add_result = int(num1) + int(num2)                     #initially num1 and num2 will be stored as string, so to add them we convert to int/float type
print(Add_result)

