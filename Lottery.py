global ammount
ammount = int(0)
global none

none = int(0)

import random
import time
#This is all the defines of to find out what the numbers where
def numbers(number1):
    if number1 == answer1:
        print("You have got",number1,"correct")
        global ammount
        ammount += 1
        
    else:
        global none
        none += 1
        
def numbers2(number2):
    if number2 == answer2:
        print("You have got ",number2,"correct")
        global ammount

        ammount += 1
        
    else:
        global none
        none += 1
        
def numbers3(number3):
    if number3 == answer3:
        print("You have got ",number3,"correct")
        global ammount
        ammount +=1
        
    else:
        global none
        none += 1
        
def numbers4(number4):
    if number4 == answer4:
        print("You have got ",number4,"correct")
        global ammount
        ammount += 1
        
    else:
        global none
        none += 1
        
def numbers5(number5):
    if number5 == answer5:
        print("You have got",number5,"correct")
        global ammount
        ammount += 1
        
    else:
        global none
        none += 1
        
        
def numbers6(number6):
    if number6 == answer6:
        print("You have got number",number6,"correct")
        global ammount
        ammount += 1
        
    else:
        global none
        none += 1
        
def numbers7(number7):
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
#Picks randoms numbers
answer1 = random.randint(0,59)
answer2 = random.randint(0,59)
answer3 = random.randint(0,59)
answer4 = random.randint(0,59)
answer5 = random.randint(0,59)
answer6 = random.randint(0,59)
answer7 = random.randint(0,59)
#Calls the defines
numbers(input("Pick your first number:"))
numbers2(input("Pick your second number:"))
numbers3(input("Pick your third number:"))
numbers4(input("Pick your Fourth number:"))
numbers5(input("Pick your fith number"))
numbers6(input("Pick your six number"))
numbers7(input("Pick your seventh number"))
#Wait's for half a second
time.sleep(0.5)
#Displayes the amount number the person got right
print("You have got",ammount,"numbers")
print("You have got",none,"wrong")


