def game():

    answer = input("Do you dare to play? (y/n) ")
    if answer.lower() != "y":
        print("Welcome to the beginning of your new world")
        start = True
        inventory = []
    else:
        print("Whatever loser, I knew you didn't have it in you anyway!")

    if start == True:
        print("Voice: Well, well well... what an interesting being you are. What's your name? ")
        player = ""


game()
