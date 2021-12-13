print("GONZALES JOHN LOUIE B. | BSCOE1-1 \n")

import random

print("WELCOME PLAYER!")
Start = "y"

def Lottery(Start):
    while Start == "y":
        firstNum = int(input("ENTER YOUR FIRST NUMBER: "))
        secondNum = int(input("ENTER YOUR SECOND NUMBER: "))
        thirdNum = int(input("ENTER YOUR THIRD NUMBER: "))
        randNum1 = random.randint(0,9)
        randNum2 = random.randint(0,9)
        randNum3 = random.randint(0,9)

        if firstNum == randNum1 and secondNum == randNum2 and thirdNum == randNum3:
            print(f"CONGRATS! YOU ARE A WINNER!")
        
        else:
            print(f"You loss :<")
            print(f"The winning numbers are: {randNum1}, {randNum2}, {randNum3}.")
            Start = input("Try again? y/n: ")

    if Start == "n":
        print("THANK YOU, BETTER LUCK NEXT TIME!")

Lottery(Start)