
# Create a dictionary

Dt = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}
print(Dt)
print("*"*100)
# Access to the value by key

print(Dt["key2"])
print("*"*100)
# Add a new element to Dt
Dt[(1,2,3)] = "Tuple"
print(Dt)
print("*"*100)

# Access to the tuple key
print(Dt[(1,2,3)])
print("*"*100)

# Get all the keys in dictionary

print(Dt.keys())
print("*"*100)

# Get all the values in dictionary

print(Dt.values())