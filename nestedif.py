a=int(input("enter a value:"))
if(a%3==0):
    if(a%5==0):
        print("the no. is divisable by 3 and 5",format(a))
    else:
        print("the no. is not divisable by 5", format(a))
else:
    print("the no. is not even divisable by 3", end=" ")

