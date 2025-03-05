print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Ask if the user wants to go left or right
#All the answers will be transformed into lower case
#Any answer that are not part of the options will lead to a game over
choice = input("Your are on a crossroad, where do you want to go?"
               'Type "left" or "right".\n').lower()

#Choice between left or right
#If they choose right they lose, if they choose left they found a lake with a island in the middle
if choice == "left":
    
    #They choose if they want to wait or swim
    #If they swim they get attacked, if they wait they survive
    choice = input("You\'ve come to a lake."
                   "There is an island in the middle of the lake."
                   'Type "wait" to wait for a boat.'
                   'Or type "swim" to swim across.').lower()
    if choice == "wait":
        
        #They find a house with 3 colored doors: red, yellow, and blue
        #The red leads to a room on fire, the blue leads to a room full of beasts
        #The winner door is the yellow one
        choice = input("You arrive at the house unharmed"
                       "In front of you there is house with three doors."
                       'Typer "red" to enter the red door'
                       'Type "yellow" to enter the yellow door'
                       'Type "blue" to enter the blue door.').lower()
        if choice == "yellow":
            print("You enter in a treasure room"
                "You win!")
        elif choice == "red":
            print("You enter the room and suddenly starts a fire!"
                  "Game over!")
        elif choice == "blue":
            print("You enter a dark room and you start to see red eyes everywhere... they are BEASTS!!!"
                  "GAME OVER!")
        else:
            print("That option doesn\'t exist."
                  "GAME OVER!")

    else:
        print("You got attacked by a trout."
              "GAME OVER!")

else:
    print("You fall into a hole."
          "GAME OVER!")