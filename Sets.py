
# Create a set
Set1 = {"pop","rock","soul","disco","rock","disco"}
print(Set1)
print("*"*100)
# Convert list to a set

L1 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
print(L1)
print(set(L1))
print("*"*100)

# Add a new element to our Set1

Set1.add("Numbers")
print(Set1)
print("*"*100)

# Remove the element from a set

Set1.remove("Numbers")
print(Set1)

# Sample sets

Set1 = {1,2,3,4,5,6,7,8,9}
Set2 = {7,8,9,0,11,12,13}
print("*"*100)

# Find the intersection between the set
print(Set1)
print(Set2)
intersection = Set1.intersection(Set2)
print(intersection)
print("*"*100)

# Find what is difference in set 1 given set 2
print(Set1)
print(Set2)
difference = Set1.difference(Set2)
print(difference)
print("*"*100)

# Find what is difference in set 2 given set 1
print(Set1)
print(Set2)
difference = Set2.difference(Set1)
print(difference)
print("*"*100)

# Union

print(Set1.union(Set2))
print("*"*100)

# Get the sum of all the elements in the list but we can not sum the same number twice
L1 = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
L2 = set(L1)
print(L2)
print(sum(L2))

artist = "Michael"
