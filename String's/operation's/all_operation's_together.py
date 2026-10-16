name = "Himesh Rupchandani"
name1 = "vishal rupchandani"
number = 123456

print("Length of name: ",len(name)) # Tell total length of string.

# endswith and startswith Both are Case-sensitive 
print("End with function: ",name.endswith("chandani")) # Always provide answer in True or False. 
print("Start with function: ",name.startswith("himesh")) # Same as a endswith() function
print("capitalize: ",name.capitalize()) # Always capitalize first letter only
print("int to string: ",str(number)) # Convert int to string

# Upper and Lower case

print("Covert lower to upper: ",name.upper()) # Conver all the character in upper case
print("Convert upper to lower: ",name.lower()) # Conver all the charater in lower case

# Title use for convert name like this
# himesh rupchandani to Himesh Rupchandani mean's it's convert in Heading form
print("title function: ",name1.title())

# Find function to find index of that word
print("Find function: ",name.find("Rupchandani")) # Here name = Himesh Rupchandnai and R is on 7th index

# replace function
print("Replace function: ",name.replace("Himesh","Karan")) # here name = Himesh Rupchandani so it replace by Karan Rupchandnai
