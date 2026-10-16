example = {
    "name" : "Himesh",
    "marks" : 100,
    "age" : 18
}

print(example)

# Add
example["surname"] = "Rupchandani"
print(example)

# Update
example["marks"] = 95
print(example)

# Delete
del example["age"]
print(example)

"""

OUTPUT:
{'name': 'Himesh', 'marks': 100, 'age': 18}
{'name': 'Himesh', 'marks': 100, 'age': 18, 'surname': 'Rupchandani'}
{'name': 'Himesh', 'marks': 95, 'age': 18, 'surname': 'Rupchandani'}
{'name': 'Himesh', 'marks': 95, 'surname': 'Rupchandani'}

"""