n=int(input("enter how any item:"))
n1,n2=0,1
count=0
if n<=0:
    print("no fibonacci for negative number")
elif n==1:
    print(n1)
else:
    print("fibonacci :", end=" ")
    while count<n:
        print(n1)
        temp=n1+n2
        n1=n2
        n2=temp
        count+=1