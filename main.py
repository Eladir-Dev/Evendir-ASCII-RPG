import os

# State variables
run = True
menu = True
play = False
show_rules = False

# Larg strings
rules = "This are the rules"

# Player Stats
name = "Player"
HP = 50
ATK = 3

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
    for i in range(length):
        print(line_char, end="")
    print()
    print(finish, end="")

def save():
    """
    This method saves the game to a file
    """
    list[
        name,
        str(HP),
        str(ATK)
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

def load():
    """
    This method loads the game from a file
    """
    f = open("load.txt", "r")
    load_list = f.readlines()
    name = load_list[0][:-1]
    HP = load_list[1][:-1]
    ATK = load_list[2][:-1]
    f.close()

# Main loop
while run:
    while menu:
        clear()
        print("""
1, New Game
2, Load Game
3, Rules
4, Quit Game""")

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
            clear()
            print(f"Welcome back, {name}!")
            input("> ")
            menu = False
            play = True
        elif choice == "3":
            show_rules = True
        elif choice == "4":
            quit()

    while play:
        print(name)

        dest = input("# ")

        if dest == "0":
            play = False
            menu = True