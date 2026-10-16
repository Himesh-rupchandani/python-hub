# Alice
list1 = [1,2,3,4]
list2 = list1

list1[0] = 10
print(list1,list2)

list2[0] = 20
print(list1,list2)

# Copy
list3 = list1.copy()
list3[0] = 25
print(list3,list1)

"""

OUTPUT:
[10, 2, 3, 4] [10, 2, 3, 4]
[20, 2, 3, 4] [20, 2, 3, 4]
[25, 2, 3, 4] [20, 2, 3, 4]

"""