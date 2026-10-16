def second_largest(list):
    largest = float('-inf')
    s_largest = float('-inf')

    for i in list:
        if i > largest:
            s_largest = largest
            largest = i
        elif i > s_largest and i < largest:
            s_largest = i
    return s_largest

list = [1,523,61,5023,1002,1,31,23,21,151,203,151,2031]
print(second_largest(list))