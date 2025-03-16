def sayhi(name):                                           #functions are defined here with a parameter and should have : after paranthesis
    print("Hello " + str(name) + ", how are you?")         #the intendation or space at the beginning of this line shows this part onwards is part of the function
    return                                                 #returns are mainly used to return back any value, here its not returning anything

sayhi("Leo")                                               #function is called here, without this the program would never go into the above part

print("Next is a summation function:")

def summation(num1,num2,num3):                             #here 3 numbers are passed to the function
    return num1+num2+num3                                  #a value is returned to the place where function was called

result = summation(15,20,40)             #function is called here and the value returned will be stored in result
print("The sum is " + str(result))

#if and else statements

is_male = False                                            #changing the boolean will print different results
is_short = False

if is_male :                                               #this will by default check for true statements

    if not(is_short) :                                     #not will change value of boolean to opposite, i.e True-False and then if statement will be checked
        print("you are a tall male")
    else :                                                 #basic else condition, it checks opposite of its if condition
        print("you are a short male")
elif not(is_male) and is_short :                           #elif is combination of if and else
    print("You are a short Female")
elif not(is_male) or not(is_short):
    print("You are either not a male or is not short or both,\nrechecking...")
if not(is_male) and not(is_short):
    print("You are a tall female")


#more if statements with operators                         # {>, <, ==, !=, >=, <=}  are the main opeartors
def max_num (num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else :
        return num3

print(max_num(100,40,5000))



#basic maths calculator
a = float(input("Enter first number "))                   #here float is given to convert the default string setting of input to float, so that the number entered can be used
operator = input("Enter the maths operator")              #here no float is used as str will help us compare the operator later on
b = float(input("Enter second number "))

if operator == "+":
    print(a+b)
elif operator == "-":
    print(a-b)
elif operator == "/":
    print(a/b)
elif operator == "*":
    print(a*b)
else :
    print("Invalid operator")
