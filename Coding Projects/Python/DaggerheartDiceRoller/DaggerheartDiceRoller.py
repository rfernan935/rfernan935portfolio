# the purpose of this program is to roll 2 d12 with optional accounting for qualities of hope and fear 
# as in Daggerheart for action or reaction rolls. the program will let the user roll as many times as 
# they'd like on one run until they press the quit button.

import random

# roll a d12 function
def rollD12():
    d12 = random.randint(1, 12)
    return d12

def rollAny(rollType) :
    # roll hope (using roll d12 function)
    hopeNum = rollD12()
    # roll fear (using rolld12 function)
    fearNum = rollD12()
    # determine number of roll
    rollNum = hopeNum + fearNum
    # return
    return hopeNum, fearNum, rollNum

# main
#start roll loop
while True:

    while True:
        userInput = input("What kind of roll are you making? Press 1 for Action, 2 for Reaction. \n")

        if userInput == '1' or userInput =='2':
            rollType = int(userInput)
            break

        else: 
            print("That is not a valid input. Try again.\n")
        
    
    currentHopeNum, currentFearNum, currentRollNum = rollAny(rollType)

    #print
    print(" Hope: ", currentHopeNum, "\n", "Fear: ", currentFearNum, "\n", "You rolled", currentRollNum, )

    if rollType == 1:
        # determine quality of roll
        if currentHopeNum > currentFearNum:
            rollQuality = " with hope."
        elif currentHopeNum < currentFearNum:
            rollQuality = " with fear."
        else:
            rollQuality = "It's a critical success!"

        # print quality
        print(rollQuality, "\n")

    contChoice = input("Roll again? Press Q to quit, or any other key to continue.\n")
    
    if contChoice == 'Q' or contChoice == 'q':
        print("Thanks for rolling!")
        break
