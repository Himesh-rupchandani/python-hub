profile = {
    "name" : "Himesh",
    "age" : 18,
    "marks" : 90,
    "surname" : "Rupchandani",
    "address" : "Rajkot"
}

# get() <------- Enter key's and got value 
print(profile.get("age"))

# keys() <-------- To print all the key's in dictionary
print(profile.keys())

# values() <---------- To print all the value's in dictionary
print(profile.values())

# items() <-------- To print all the items (key's and value's both)
print(profile.items())

# pop() <------- To remove specific key and value and always's enter key's in ()
profile.pop("age")
print(profile.items())

# popitem() <---- To remove last value of dictionary
profile.popitem()
print(profile.items())

# clear() <----- To Erace everything
profile.clear()
print(profile.items())


"""

OUTPUT:

18
dict_keys(['name', 'age', 'marks', 'surname', 'address'])
dict_values(['Himesh', 18, 90, 'Rupchandani', 'Rajkot'])
dict_items([('name', 'Himesh'), ('age', 18), ('marks', 90), ('surname', 'Rupchandani'), ('address', 'Rajkot')])
dict_items([('name', 'Himesh'), ('marks', 90), ('surname', 'Rupchandani'), ('address', 'Rajkot')])
dict_items([('name', 'Himesh'), ('marks', 90), ('surname', 'Rupchandani')])
dict_items([])

"""