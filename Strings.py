# Assign a string to a variable
Name = "Hello World"
print(Name)

# Print the first element in the string
print(Name[0])

# Print the last position in the string
print(Name[-1])

# Find the length of the Name variable

print(len(Name))

#Lets just get the "Hello" word

print(Name[0:5])

#Lets get the "world" word and assign it to a variable

World = Name[6:]
print(World)

# Lets get every second element
print(Name[::2])

# Lets get every second element in the range from index 0 to index 4
print(Name[0:4:2])

# Concatena two strings
Name = "Hello "

Hello_world = Name + "World"
print(Hello_world)

# Multiplication operand

print("Hello World "*10)
print("*"*100)

# Convert all the characters in string to upper case
A = "Hello World"
print("Before upper: ", A)
B = A.upper()
print("After upper: ", B)
print("*"*100)

# Replace the word "World" with "Universe"

A = "Hello World"
print(A)
B = A.replace("World", "Universe")
print(B)

# Find H, W, d characters inside A variable
print(A.find("H"))
print(A.find("W"))
print(A.find("d"))
print(A.find("o"))
print(A.find("World"))

