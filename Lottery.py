global ammount
ammount = int(0)
global none

none = int(0)

import random
import time
#This is all the defines of to find out what the numbers where
def numbers():
    if number1 == answer1:
        print("You have got",number1,"correct")
        global ammount
        ammount += 1
        
    else:
        global none
        none += 1
        
def numbers2():
    if number2 == answer2:
        print("You have got ",number2,"correct")
        global ammount

        ammount += 1
        
    else:
        global none
        none += 1
        
def numbers3():
    if number3 == answer3:
        print("You have got ",number3,"correct")
        global ammount
        ammount +=1
        
    else:
        global none
        none += 1
        
def numbers4():
    if number4 == answer4:
        print("You have got ",number4,"correct")
        global ammount
        ammount += 1
        
    else:
        global none
        none += 1
        
def numbers5():
    if number5 == answer5:
        print("You have got",number5,"correct")
        global ammount
        ammount += 1
        
    else:
        global none
        none += 1
        
        
def numbers6():
    if number6 == answer6:
        print("You have got number",number6,"correct")
        global ammount
        ammount += 1
        
    else:
        global none
        none += 1
        
def numbers7():
    if number7 == answer7:
        print("You have got number",number7,"correct")
        global ammount
        ammount += 1
        
    else:
        global none
        none += 1
        

#Welcomes to the program    
print("Welcome to the lottery")
#Lets the user pick the numbers
number1 = input("Pick your first number:")
number2 = input("Pick your second number:")
number3 = input("Pick your third number:")
number4 = input("Pick your Fourth number:")
number5 = input("Pick your fith number")
number6 = input("Pick your six number")
number7 = input("Pick your seventh number")
#Picks randoms numbers
answer1 = random.random()
answer2 = random.random()
answer3 = random.random()
answer4 = random.random()
answer5 = random.random()
answer6 = random.random()
answer7 = random.random()
#Calls the defines
numbers()
numbers2()
numbers3()
numbers4()
numbers5()
numbers6()
numbers7()
#Wait's for half a second
time.sleep(0.5)
#Displayes the amount number the person got right
print("You have got",ammount,"numbers")
print("You have got",none,"wrong")


