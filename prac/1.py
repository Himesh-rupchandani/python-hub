n = int(input(("Enter a number for factorial: ")))

ans = 1
i = 1
# for i in range(1,n+1):
#     ans = ans * i

while i<=n:
    ans = ans * i
    i += 1

print("Factorial number is: ",ans)