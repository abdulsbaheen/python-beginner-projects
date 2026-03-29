# Snake water gun game
import random

print("WELCOME TO SNAKE, WATER, GUN GAME.")
print("LEt's Start game !")
print("Rules:")
print("Snake drinks Water")
print("Water drowns Gun")
print("Gun kills Snake")
print("----------------------------------")

choices =["snake","water","gun"]
print('''choices:
 1.snake
 2.water
 3.gun''')
user_ch=input("Enter you choice :")
comp_ch=random.choice(choices)


print("You chose:", user_ch)
print("Computer chose:", comp_ch)

if user_ch not in choices:
    print ("invaid input ! please enter valid input")
elif user_ch == comp_ch:
    print ("Its a tie !")
elif (user_ch == "snake" and comp_ch == "water") or \
     (user_ch == "water" and comp_ch == "gun") or \
     (user_ch == "gun" and comp_ch == "snake"):
    print("You win!")
else:
    print("You lose!")