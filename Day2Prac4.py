data = {
    "Roy": "0909123456",
    "April": "0912345",
    "Randy": "456-888",
    "Vee": "331-3324"
}
ch = ""
while ch.lower() != "x":
    print("Simple PhoneBook")
    print("[V] - View All Data")
    print("[S] - Search for Specific Data")
    print("[X] - Exit")
    ch = str(input("Enter Choice: "))

    if ch.lower() == "v":
        for v in data:
            print(f"{v} - {data[v]}")
        input("Press any key to continue...")
    elif ch.lower() == 's':
        search = input("Input name: ").title()
        print(f"{search} - {data.get(search, 'Does not exists')}")
        input("Press any key to continue...")
    elif ch.lower() == "x":
        exit()
    else:
        print("Unknown!")
