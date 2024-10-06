# set - use to store multiple data - unordered and unindexed
fruits = {"apple", "banana", "avocado"}

if "apple" in fruits:
    print("Available")

# union method
set_a = {1,2,3}
set_b = {4,5,6,1}
union_set = set_a.union(set_b)
print(union_set)

#intersection
intersect_set = set_a.intersection(set_b)
print(intersect_set)

# difference
diff_set = set_a.difference(set_b)
print(diff_set)

# symetric diff
sym_diff = set_a.symmetric_difference(set_b)
print(sym_diff)