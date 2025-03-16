'''
sometimes the code may show an error and the code will break due to the error. try and except will help the program
inform the user that the program is stuck at a point, maybe due to a user input and will give a prompt
'''

try :
    #block = 10/0                                           #is this statement is not commented out, it will show a division by zero error
    number = int(input("Enter a number: "))                 #the input is to be converted to an int, so any string input will be an error and program normally will break here, hence we have used try and except here.
    print(number)
except ZeroDivisionError as error:                          #if zero division error is present in code, this part will recognise it and print it as the error
    print(error)
except ValueError:                                          #Value error is shown when a wrong value is input by user,i.e here if user inputs a string instead of a number
    print("Invalid input")

#important to remember that if we just use except without mentioned what condition, any code in the prograam that comes
#outside try: will be seen as an exception, even if that part of the coed is wrong. For example if the 10/0 division is outside try, and
# if the coder has not specified an except: with ZeroDivisionError, then the program will just try executing that division and will break due to error

#Commenting
# <- this hash symbol means whatever you type after this is taken as a comment and is not code for the program
''' 
a comment can also be represented using 3 ' as in this para and also at the beginning of this file
'''
