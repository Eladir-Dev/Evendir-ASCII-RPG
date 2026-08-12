import os

run = True
menu = True
play = False
show_rules = False

# Stats
HP = 50
ATK = 3

def clear():
    os.system("cls")

def draw(length :int, char :str):
    """
    This method draws a line
    """
    for i in range(length):
        print(char, end="")
    print()

def save():
    list[
        name,
        str(HP),
        str(ATK)
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

rules = "This are the rules"

while run:
    while menu:
        clear()
        Print("""
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
            f = open("load.txt", "r")
            load_list = f.readlines()
            name = load_list[0][:-1]
            HP = load_list[1][:-1]
            ATK = load_list[2][:-1]
            f.close()
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