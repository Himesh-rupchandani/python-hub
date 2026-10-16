numbers = [12,-5,45,150,-8,30,0,25]

for i in range(0,len(numbers)):
    if numbers[i] == 0:
        break
    elif numbers[i] < 0:
        continue
    elif numbers[i] > 100:
        pass
    else:
        print(numbers[i])