from flask import Flask, render_template

app = Flask(__name__, template_folder='C:/Users/plann/Desktop/Prac/')

@app.route('/')
def index():
    print('''
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
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
    #Write your code below this line 👇
    path=input('You are at a crossroad. Where do you want to go? Type "left" or "right"')
    path1=path.lower()
    if path1=="left":
        t=input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
        t1=t.lower()
        if t1=="wait":
            door=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
            door1=door.lower()
            if door1=="red":
                return "Burned by fire. Game Over"
            elif door1=="blue":
                return "You enter a room of beasts. Game Over."
            elif door1=="yellow":
                return "You found the treasure! You Win!"
            else:
                return "You chose a door that doesn't exist. Game Over."
        elif t1=="swim":
            return "You are under attacked"
        else:
            return "Wrong input.Game Over."
    elif path1=="right":
        return "You fell into a hole. Game Over."
    else:
        return "You typed wrong direction. Game Over."

if __name__ == '__main__':
    app.run(debug=True)
