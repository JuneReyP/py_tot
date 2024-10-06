
ch = ""
word = list()
while ch.lower() != "n":
    input1 = input("Enter a word: ")
    word.append(input1)
    check = input("Try again? Y/N: ")
    if check.lower() == "n":
        break
    elif check.lower() == "y":
        input("Press any key to continue...")
    else:
        input("Invalid...")
        break

print(f"Number of words input: {len(word)}")
# print(f"Count: {word.count()}")
for i in word:
    print(i)
