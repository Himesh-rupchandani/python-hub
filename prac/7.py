list = [1,0,20,30,60,99,85,6,523,253,5]

maxx = 0
for i in range(0,len(list)):
    if list[i] > maxx:
        maxx = list[i]

print(maxx)