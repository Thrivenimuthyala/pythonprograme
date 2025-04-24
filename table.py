# #any multicat table
# for i in range(1,11):
#     for j in range(1,11):
#         product=i*j
#         print(i,"x",j,"=",product)
#     print("-"*20)
#     while
from itertools import product

numbers=int(input("enter:"))
i=1
while i<=10:
    product=numbers*i
    print(numbers, "x", i, "=", product)
    i+=1