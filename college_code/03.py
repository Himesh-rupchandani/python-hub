""" Write a program that uses a for loop to print all the odd, even numbers in the range input by user. """


x = int(input("Enter a number for total range: "))

# Odd number's
print("\nList of my all Odd number in range x:")
for i in range(0,x):
    if i%2!=0:
        print(i,end=" ")
print("\n")
    
# Even Number
print("List of my all Even number in range x:")
for i in range(0,x):
    if i%2==0:
        print(i,end=" ")


"""

Enter a number for total range: 10

List of my all Odd number in range x:
1 3 5 7 9 

List of my all Even number in range x:
0 2 4 6 8 

"""
