#Dictionaries are like a class, certain information is stored and each info has a unique key. The info is accessed in the program using the key
#these are also called hash tables
months = {                                               # Dictionaries are notated with {}, also use = as same as list or tuple for assigning value into dictionary
    1 : "January",                                       #Seperating entries using ',' is important, similar to list
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    "Oct" : "October",                                   #The key can be either numbers or strings, it only has to be unique
    "Nov" : "November",
    "Dec" : "December",
}

print(months[1])                                         #here, inside[] its not the index number, it is the key. so 1 will print January,not February
print(months.get("Dec"))                                 #get() function can also give a certain value from dictionary according to key
print(months.get(12,"Not a Valid Key"))                  #with get(), if an invalid key is entered, we can see that by giving a statement as the second parameter. Else it will display 'None'


# Now we will see usage of modules and pip
# Modules are python libraries. Some of these are inbuilt into python, others pre loaded in the version of python and can
# be accessed in the left hand side panel, under Project\Extended Libraries\Lib. These libraries can be imported into the
# current program, so that you do not have to write the code from scratch.

#import numpy as np                                      #here we have imported numpy module, which is used for n dimensional array calculations
import random                                            #random module helps us use random function, such as for getting a random output
#import matplotlib                                       #this module allows to visualise using data given, such as plotting, animation etc


'''pip installing a module is used to install third party modules outside python into python for using with our code. 
to pip, go to your PC's command prompt and check if a version of pip is installed by typing 'pip --version' and enter. The Command prompt will
show the version of pip. Now you can use google to look for various 3rd party modules. Here I have tried Matplotlib. To pip this, again go to command prompt
and type 'pip install matplotlib' and enter. The module will be installed and you can import it into your code'''