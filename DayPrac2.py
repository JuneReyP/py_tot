import random

res = ""
response = tuple(("p","r","s"))
while res.lower() != "x":
    print("Jack n Poy Game")
    print("Computer VS User")
    print("Legend: ")
    print("[P/p] - Paper")
    print("[R/r] - Rock")
    print("[S/s] - Scissor")
    print("[X/x] - Exit")

    user = str(input("Enter user's bet: "))
    c = random.randint(0,2)
    computer = response[c]

    if user.lower() == "p" and computer == "r":
        print(f"Computer: {computer}")
        print("User Wins! Paper covers Rock.")
    elif user.lower() == "r" and computer == "p":
        print(f"Computer: {computer}")
        print("Computer Wins! Paper covers Rock.")

    elif user.lower() == "p" and computer == "s":
        print(f"Computer: {computer}")
        print("Computer Wins! Scissor cuts Paper.")
    elif user.lower() == "s" and computer == "p":
        print("User Wins! Scissor cuts Paper.")

    elif user.lower() == "r" and computer == "s":
        print(f"Computer: {computer}")
        print("User Wins! Scissor cannot cut Rock.")
    elif user.lower() == "s" and computer == "r":
        print(f"Computer: {computer}")
        print("Computer Wins! Scissor cannot cut Rock.")
    elif user.lower() == "x":
        exit()
    else:
        print("Invalid input")

    input("Press any key to continue...")

