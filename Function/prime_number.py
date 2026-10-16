def prime(n):
    if n<=1:
        print("Number is not prime number")
        return

    flag = False
    for i in range(2,n):

        if(n%i==0):
            print("Number is not a prime number.")
            flag = True

    if(flag==False):
        print("Number is prime number.")

n = int(input("Enter a number: "))
prime(n)