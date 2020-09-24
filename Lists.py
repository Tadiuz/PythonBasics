# Create a list

L = ["Strings",12,2.3,[1,2,3,4],("Tuples",2)]
print("*"*100)

# Use the extend method to add elements to a list
print(L)
L.extend(["Games",10])
print(L)

print("*"*100)
# Use the append method to add elements
L = ["Strings",12,2.3,[1,2,3,4],("Tuples",2)]
print(L)
L.append("Games")
L.append(10)
print(L)
print("*"*100)

# Use the same method
L = ["Strings",12,2.3,[1,2,3,4],("Tuples",2)]
print(L)
L.append(["Games",10])
print(L)
print("*"*100)

# Change the first element of the given list
L = ["Strings",12,2.3,[1,2,3,4],("Tuples",2)]
print(L)
L[0] = "Words"
print(L)
print("*"*100)

#Delete elements of the list
L = ["Strings",12,2.3,[1,2,3,4],("Tuples",2)]
print(L)
del(L[0])
print(L)
print("*"*100)

# Assign a list to another list

L1 = [1,2,3,4,5,6,7,8]
L2 = L1
print("List 1 is: ",L1)
print("List 2 is: ",L2)
L1[0] = 0
print("New List 1 is: ",L1)
print("New List 2 is: ",L2)
print("*"*100)

# Clone a list
L1 = [1,2,3,4,5,6,7,8]
L2 = L1[:]
print("List 1 is: ",L1)
print("List 2 is: ",L2)
L1[0] = 0
print("New List 1 is: ",L1)
print("New List 2 is: ",L2)
print("*"*100)

# Negative index slicing
L1 = [1,2,3,4,5,6,7,8]

print(L1[::-1])
print("*"*100)

# String
Word = "Hello World"
print("Reversed word: ", Word[::-1])









