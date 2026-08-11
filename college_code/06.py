# Write a program to demonstrate working with tuples in python.

number = (1,1,12,3,50,99)

# Finding Length of Tuple uding len()
print("Length of my tuple is:",len(number))

# Finding minimum & maximum number in Tuple using min() & max()
print("Minimum number in my Tuple is: ",min(number))
print("Maximum number in my Tuple is: ",max(number))

# Counting any element in tuple like how many times is repeting using count()
print(f"1 is repeted in Tuple for {number.count(1)} times")

# Finding index of any value using index()
print(f"Index of 50 in Tuple is {number.index(50)}")

# Arrengging value's in accending order using sorted()
new_number = sorted(number)
print("My sorted Tuple is: ",new_number)


#OUTPUT:-
"""

Length of my tuple is: 6
Minimum number in my Tuple is:  1
Maximum number in my Tuple is:  99
1 is repeted in Tuple for 2 times
Index of 50 in Tuple is 4
My sorted Tuple is:  [1, 1, 3, 12, 50, 99]

"""
