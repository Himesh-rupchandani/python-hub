name = "Himesh Rupchandani"

print(name[1:5:2]) 

# Here start with 1st index.
# Than goes 1 to 5-1=4 index mean's imes.
# Than we skip 2 index like i skip,skip e skip,skip and over.
# Rember we start skipping from index where we start our slicing.

# Advanced slicing
print(name[:len(name)]) # If nothing written in starting of slicing than it's start with 0 index always.
print(name[0:])         # If nothing written in ending of slicing thjan it's end with len(variable) always.