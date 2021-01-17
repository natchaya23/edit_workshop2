# example 1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # ['apple, 'cherry']

# example 2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# example 3
# thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# example 4
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# example 5
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)