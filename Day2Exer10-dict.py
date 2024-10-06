# dictionary - used to store data values in key:value pairs. is a collection which is unordered, changeable and does not allow duplicates.
data = ["apple", "banana", "apple", "banana", "cherry", "banana", "kiwi", "kiwi"]

count_dict = {}
for item in data:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print("Occurrences: ", count_dict)

# config = {
#     "host": "localhost",
#     "port": 8080,
#     "debug": True
# }
# print("Host: ", config['host'])
# print("Port: ", config['port'])
# print("Debug: ", config['debug'])
# for v in config:
#     print(f"{v.title()}: {config[v]}")
#
# for k, v in config.items():
#     print(f"{k.title()}: {v}")

# code_to_name = {
#     101: "Alice",
#     102: "Bob",
#     103: "Charlie"
# }
#
# code = 104
# print(f"Name with 104 code: {code_to_name.get(code,'Unknown code!')}")