# try:
#     fw = open("file2.txt", "w") # w = write/overwrite
#     content = "1003#James Gosling#25000#4231"
#     fw.write(content+"\n")
#     print("Successful.")
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     fw.close()

# try:
#     fw = open("file2.txt", "a") # a = append/add
#     content = "1005#Jet Li#55000#1221"
#     fw.write(content+"\n")
#     print("Successful.")
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     fw.close()