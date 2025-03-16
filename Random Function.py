#here we show some random functions and how they are used in code
import random                                                    #we are importing the random module.
random_integer = random.randint(0,5)                       #randint(a,b) is a function when used as shown will give a random integer btw a & b, both a and b included!!
print(random_integer)
random_float = random.random()                                   #this gives a random floating point number in [0.0-1.0),1 not included!!
print(random_float)

new_random = random_float + random_integer                       #if we want to print floating points between numbers outside 0 and 1, then combine these two as shown.
print(new_random)

#lets see how a random output function such as acoin toss can be coded.
random_side = random.randint(0,1)
if random_side == 1:
    print("Heads")
else :
    print("Tails")

coin = ["heads", "tails", "middle"]

print(random.choice(coin))                                       #choice() will give random choices out of a listof numbers or strings

