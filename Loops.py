# For loop example

Numbers = [1,2,3,4,5,6,7,8,9]
Length = len(Numbers)

for i in range(Length):
    print(Numbers[i])

print("*"*100)
# Lets iterate over our list
for element in Numbers:
    print(element)
print("*"*100)

# Sequence of numbers using range function

for i in range(5):
    print(i)
print("*"*100)
# Sequence of numbers using range function with starting number

for i in range(5,50):
    print(i)
print("*"*100)

# Sequence of numbers using range function

for i in range(5,50,4):
    print(i)
print("*"*100)

# Use enumerate function
Color = ["Red","Blue","Purple","Yellow","Black"]

for i, s in enumerate(Color):
    print(i, ": ", s)
print("*" * 100)
# While loop example
date = [1982, 1980, 1973, 2000]

i = 0
year = 0

while (year!=1973):
    year = date[i]
    i = i+1
    print(year)

print("*" * 100)

# Break keyword
#Lets say that we have our variable equal to zero
i = 0
while True:
    print(i)
print("*" * 100)
