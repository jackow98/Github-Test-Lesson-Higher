import random

terms = ["LAN"]
definitions = ["Local Area Network covers small geographical area"]

def start_quiz(terms, definitions):
    choice = "y"
    while choice == "y":
        randomPosition = random.randint(0, len(terms)-1)
        print(terms[randomPosition])
        input("Press enter to continue")
        print(definitions[randomPosition])
        choice = input("Continue Y or N")

def showMenu():
    print("1. Start Quiz or 2. Exit")
    userInput = input("Enter option: ")
    while userInput !="1" and userInput != "2":
        print("Invalid input, try again")
        userInput = input("Enter option: ") 
    if userInput == "1":
        start_quiz(terms, definitions)
    else:
        print("CYA L8r")  

showMenu()

