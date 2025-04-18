a=[20,30,'abc',"true",13.6]
b=[20,30,'abc','true',13.6]
c=b
print(a is b)
print(b is c)
print(a is not c)
print(a is not b)