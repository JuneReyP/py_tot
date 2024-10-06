# file = open("",[r,a,w,x]) # r = read, a = append, w = write, x = create

# try:
#     fr = open("file.txt","r")
#     content = fr.read()
#     print("Content: \n",content)
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     fr.close()

try:
    fr = open("file.txt","r")
    for line in fr:
        line = line.strip("\n") # remove new line character
        line = line.strip(" ")  # remove new line character
        mylist = line.split("#") # split the line by #

        # print(mylist)
        print(f"Account No: {mylist[0]}")
        print(f"Account Name: {mylist[1]}")
        print(f"Account Balance: {mylist[2]}")
        print(f"PIN: {mylist[3]}")
        print("----------------------------")
except FileNotFoundError:
    print("File not found.")
finally:
    fr.close()