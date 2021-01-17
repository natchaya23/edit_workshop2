thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Ex1
for key in thisdict:
    print(key)

# Output:
# brand
# model
# year
print("------------------------------------------")


thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Ex2
for key in thisdict:
    print(thisdict[key])

# Output:
# ford
# Mustang
# 1964
print("------------------------------------------")


thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Ex3
for key in thisdict.keys():
    print(key)

# Output:
# brand
# model
# year
print("------------------------------------------")

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Ex4
for value in thisdict.values():
    print(value)

# Output:
# ford
# Mustang
# 1964
print("------------------------------------------")


thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Ex5
for key, value in thisdict.items():
    print(key, value)

# Output:
# drand ford
# model Mustang
# year 1964