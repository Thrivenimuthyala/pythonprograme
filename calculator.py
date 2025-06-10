num1=int(input("enter first item:"))
ope=input("enter operator:")
num2=int(input("enter second item:"))
if ope=="+":
    print(num1+num2)
elif ope=="-":
    print(num1 - num2)
elif ope=="/":
    print(num1 / num2)
elif ope=="%":
    print(num1%num2)
else:
    print("wrong operator")
