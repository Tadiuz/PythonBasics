# First tuple
Tuple1 = ("musics",10,2.5)
print(Tuple1)
print(type(Tuple1))
print("*"*100)

# Concatenate two tuples

Tuple2 = Tuple1 + ("games",10)
print(Tuple2)

# Slice from index 0 to index 2
print(Tuple2[0:2])
print("*"*100)

# Get the length of the tuple
print(len(Tuple2))
print("*"*100)

# Create a tuple with numbers and sort it

Rating = (2,3,4,5,4,34,32,54,65,34,2300)
print(sorted(Rating))
print(type(sorted(Rating)))
print("*"*100)

# Lets declare a nested tuple

Nested = (1,2,3,4,5,("Hello","World",(11,12,13)))
print(Nested)
print("*"*100)

#Print the elements

print(Nested[0])
print(Nested[-1])
print(Nested[-1][0])
print(Nested[-1][-1])
print(Nested[-1][-1][0])
