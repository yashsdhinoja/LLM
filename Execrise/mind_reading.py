import random

while True:
    print("----- Welcome to AI Mind Reading Project -----")

    number = int(input("Think of a number (1 - 10) : "))
    if number < 1 or number > 10: 
        print("Please Enter a Number Between (1 to 10) : ") 
        continue

    ai = random.randint(1,10)

    print("Ai is thinking.....")
    print("Your Number : ", number)
    print("Ai Guessed : ", ai)

    if number == ai:
        print("Ai read your mind.")
    else:
        print("You win this Game.")

    choice = input("Do you want play again (yes / no) : ")
    if choice.lower() == "no":
        print("Thanks for Playing.")
        break