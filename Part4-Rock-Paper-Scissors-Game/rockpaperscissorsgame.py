#Preset the graphics of the choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Importing the random library for the use of random functions
import random

#Create a list of the options
game_images = [rock, paper, scissors]

#First the player chooses is option, then the program randomizes theirs (between 0, 1 and 2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n As.:"))
pc_choice = random.randint(0, 2)

#Print the player choice and then the computer choice
print("The computer choosed:")
print(f"{game_images[pc_choice]}")

print("The player choosed:")
print(f"{game_images[player_choice]}")

#if a player insert an invalid number
if player_choice >= 3 and player_choice < 0:
    print("You typed an invalid number. You lose!!")
#In case that both pick the same
elif player_choice == pc_choice:
    print("It's a draw!!")

#In case one pick Rock(0) and the other picks Scissors(2)
elif player_choice == 0 and pc_choice == 2:
    print("You win!!")
elif player_choice == 2 and pc_choice == 0:
    print("You lose!!")

#In the other outcomes the one o picks the higher number wins
elif player_choice > pc_choice:
    print("You win!!")
else:
    print("You lose!!")