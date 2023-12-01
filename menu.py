import os,sys

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        os.system('cls')
        setup_game()

    elif option.lower() == ("help"):
        os.system('cls')
        help_menu()

    elif option.lower() == ("credit"):
        os.system('cls')
        credit_menu()

    elif option.lower() == ("quit"):
        sys.exit()

    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid comand")
        option = input("> ")

        if option.lower() == ("play"):
            os.system('cls')
            setup_game()# placeholder until written

        elif option.lower() == ("help"):
            os.system('cls')
            help_menu()

        elif option.lower() == ("credit"):
            os.system('cls')
            credit_menu()

        elif option.lower() == ("quit"):
            sys.exit()

def setup_game():
    print("So yes this is it.")

def help_menu():
    print("There is none. Ask the devs")
    print("play")
    print("credits")
    print("quit")
    title_screen_selections()

def credit_menu():
    print("Gian Cyrus F. Salvador, Fredmar Declas, Doniele Arys Antonio, Claudio Van Likigan")
    print("play")
    print("help")
    print("quit")
    title_screen_selections()

def title_screen():
    print(""" 
 _                             _   _                  __ _                
| |                           | | | |                / _(_)               
| |    _   _ _ __  _   _ ___  | | | | ___ _ __   ___| |_ _  ___ _   _ ___ 
| |   | | | | '_ \| | | / __| | | | |/ _ \ '_ \ / _ \  _| |/ __| | | / __|
| |___| |_| | |_) | |_| \__ \ \ \_/ /  __/ | | |  __/ | | | (__| |_| \__ |
\_____/\__,_| .__/ \__,_|___/  \___/ \___|_| |_|\___|_| |_|\___|\__,_|___/
            | |                                                           
            |_|                                                           """)
    print("                    play")
    print("                    help")
    print("                   credit")
    print("                    quit")
    title_screen_selections()

title_screen()