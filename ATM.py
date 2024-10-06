from os import system
from ATMpackages import process as p

#====Main Program======
ch = ""
tries = 0
global balance, acct


while ch.upper() != "X":
    if tries >= 3:
        print("Your account is temporarily disabled")
        break
    else:
        print(f"No of tries: {tries}")
        pin = str(input("Enter PIN: "))
        found = False
        name = ""
        acct = int()
        try:
            # fr = open("./account.txt", "r")
            # for line in fr:
            #     line = line.strip("\n")
            #     line = line.strip()
            #     data = line.split("#")
            #     if data[1] == pin:
            #         found = True
            #         name = data[2]
            #         balance = float(data[3])
            #         acct = data[0]
            # fr.close()
            p.test(pin)
        except FileNotFoundError:
            print("File does not exist")

        if found:
            print(f"Welcome {name}")
            ch = ""
            while ch.upper() != "X":
                p.menu()
                ch = str(input("Enter your choice: "))
                if ch.upper() == "C":
                    system('cls')
                    print("Current Balance")
                    print(f"Your current balance is {balance}")
                elif ch.upper() == "D":
                    system('cls')
                    p.deposit(balance, acct)

                elif ch.upper() == "W":
                    system('cls') # clear screen
                    p.withdraw(balance, acct)
                elif ch.upper() == "X":
                    break
                input("Press any key to continue")
        else:
            print("Invalid PIN")
        tries+=1