numbers = (10,20,30,20,40,20)

# n = numbers.count(20)
# print(n)

# m = numbers.index(30)
# print(m)

n = 20
n_count = 0
m = 30
for i in range(0,len(numbers)):
    if n == numbers[i]:
        n_count += 1
print(n_count)
   

for i in range(0,len(numbers)):
    if m == numbers[i]:
        print(i)
        break
