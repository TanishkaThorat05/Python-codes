# 1. Create and Access Set Elements
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Accessing elements using loop
print("Elements of Set 1:")
for element in set1:
    print(element)

# 2. Union of Set Elements
union_set = set1.union(set2)
print("Union of sets:", union_set)

# 3. Intersection of Set Elements
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# 4. Difference of Set Elements
difference_set = set1.difference(set2)
print("Difference of Set1 - Set2:", difference_set)