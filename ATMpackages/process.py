global balance, found, name, acct
def menu():
    print("ATM TRANSACTIONS")
    print("[C] - Check Balance")
    print("[D] - Deposit")
    print("[W] - Withdraw")
    print("[X] - Exit")

def withdraw(balance, acct):
    withdraw = int(input("Enter amount: "))
    if withdraw % 100 == 0 and withdraw <= balance:
        balance = balance - withdraw

        # checking the account and changing the account balance
        try:
            temp = str()  # temporary variable
            fr = open("./account.txt", "r")
            for line in fr:
                line = line.strip("\n")
                line = line.strip()
                data = line.split("#")
                if data[0] == acct:
                    # changing the account balance
                    temp = temp + data[0] + "#" + data[1] + "#" + data[2] + "#" + str(balance) + "\n"
                else:
                    temp = temp + data[0] + "#" + data[1] + "#" + data[2] + "#" + data[3] + "\n"
            fr.close()

        except FileNotFoundError:
            print("File does not exist")

        try:
            fr = open("./account.txt", "w")
            fr.write(temp)
            fr.close()
        except FileNotFoundError:
            print("File does not exist")

        print("Withdrawal Successful")
        print(f"Your current balance is {balance}")

def deposit(balance, acct):
    print("Deposit")
    amt = int(input("Enter amount: "))
    if amt < 0:
        print("Invalid Amount")
        print("Cannot accept negative amount")
    else:
        balance = balance + amt
        # checking the account and changing the account balance
        try:
            temp = str()  # temporary variable
            fr = open("./account.txt", "r")
            for line in fr:
                line = line.strip("\n")
                line = line.strip()
                data = line.split("#")
                if data[0] == acct:
                    # changing the account balance
                    temp = temp + data[0] + "#" + data[1] + "#" + data[2] + "#" + str(balance) + "\n"
                else:
                    temp = temp + data[0] + "#" + data[1] + "#" + data[2] + "#" + data[3] + "\n"
            fr.close()

        except FileNotFoundError:
            print("File does not exist")

        try:
            fr = open("./account.txt", "w")
            fr.write(temp)
            fr.close()
        except FileNotFoundError:
            print("File does not exist")

def test(pin):
    fr = open("./account.txt", "r")
    for line in fr:
        line = line.strip("\n")
        line = line.strip()
        data = line.split("#")
        if data[1] == pin:
            found = True
            name = data[2]
            balance = float(data[3])
            acct = data[0]
    fr.close()
