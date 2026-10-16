friends = {
    "first" : "Shankar",
    "second" : "Rudra",
    "Third" : "Souvik",
    "Fourth" : "Tirth",
    "Fifth" : "Niv"
}

for i in friends.keys():
    print(i)

print("\n")

for i in friends.values():
    print(i)

print("\n")

for i in friends.items():
    print(i)

"""

OUTPUT:

first
second
Third
Fourth
Fifth


Shankar
Rudra
Souvik
Tirth
Niv


('first', 'Shankar')
('second', 'Rudra')
('Third', 'Souvik')
('Fourth', 'Tirth')
('Fifth', 'Niv')


"""