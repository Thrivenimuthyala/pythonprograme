n=int(input(("enter:")))
fact=1
if n<0:
    print("factorial does not exist for negative number")
elif n==0:
    print("1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print(f'the factorial of {n} is {fact}')