# Ex1
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)
# Output: {'brand', 'ford', 'year': 1964}

# Ex2
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()
print(thisdict)
# Output: #Output: {'brand', 'ford', 'model': 'Mustang'}

# Ex3
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)
# Output: {'brand', 'ford', 'year': 1964}

# Ex4
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)
# Output: {}
