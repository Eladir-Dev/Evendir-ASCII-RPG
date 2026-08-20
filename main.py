import os

# State variables
run = True
menu = True
play = False
show_rules = False

# World variables
key = False

    #   x = 0       x = 1     x = 2     x = 3     x = 4     x = 5      x = 6
map = [["plains", "plains", "plains", "plains", "forest", "mountain",     "cave"], # y = 0
       ["forest", "forest", "forest", "forest", "forest", "hills",    "mountain"], # y = 1
       ["forest", "plains", "plains", "plains", "forest", "forest",       "cave"], # y = 2
       ["forest", "plains", "plains", "plains", "forest", "hills",        "cave"], # y = 3
       ["plains", "shop",   "town",   "major",  "forest", "mountain",     "cave"], # y = 4
       ["plains", "plains", "plains", "plains", "forest", "hills",        "cave"], # y = 5
       ["plains", "fields", "fields", "plains", "hills",  "mountain", "mountain"]] # y = 6

y_len = len(map)-1
x_len = len(map[0])-1

print(y_len, x_len)

# Larg strings
rules = "This are the rules"
menu_text = """1, New Game
2, Load Game
3, Rules
4, Quit Game"""

# Player Stats
name = "Player"
HP = 50
ATK = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0

# Utilitie functions
def clear():
    """
    This method clears the screen
    """
    # Moves cursor to home position and clears the screen
    print("\033[H\033[2J", end="")

def draw(length=10, line_char="-", start="+", finish="+"):
    """
    This method draws a line
    """
    print(start, end="")
    print(line_char * length, end="")
    print(finish)

def save():
    """
    This method saves the game to a file
    """
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(f"{item}\n")
    f.close()

def load():
    """
    This method loads the game from a file
    """
    print(name)
    try:
        
        f = open("load.txt", "r")
        load_list = f.readlines()
        if len(load_list) == 9:
            name = load_list[0][:-1]
            HP = load_list[1][:-1]
            ATK = load_list[2][:-1]
            pot = int(load_list[3][:-1])
            elix = int(load_list[4][:-1])
            gold = int(load_list[5][:-1])
            x = int(load_list[6][:-1])
            y = int(load_list[7][:-1])
            key = bool(load_list[8][:-1])
            clear()
            print(f"Welcome back, {name}!")
            input("> ")
            menu = False
            play = True
        else:
            print("Saved game is corrupted.")
        f.close()
    except OSError:
        print("No saved game found.")
    

# Main loop
while run:
    while menu:
        clear()
        draw()
        print(menu_text)
        draw()

        if show_rules:
            print(rules)
            show_rules = False
            choice = input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            clear()
            name = input("# Person. What is your name! ")
            menu = False
            play = True
        elif choice == "2":
            load()
            
            # f = open("load.txt", "r") 
            # load_list = f.readlines() 
            # name = load_list[0][:-1] 
            # HP = load_list[1][:-1] 
            # ATK = load_list[2][:-1]
            # f.close()

        elif choice == "3":
            show_rules = True
        elif choice == "4":
            quit()

    while play:
        # print(name)
        draw()
        print("0 - Save and Quit")
        draw()
        save()

        dest = input("# ")

        if dest == "0":
            play = False
            menu = True