# n=int(input("enter the number of elements: "))
# array=[]
# for i in range(n):
#     element=int(input("enter element {}:"))
#     array.append(element)
# print(array)

# n=int(input("enter the number of elements: "))
# array=[]
# for i in range(n):
#     element=int(input("enter element:"))
#     array.append(element)
# print(array)
# sum=0
# for element in array:
#     sum+=element
# print("sum of all the elements:",sum)

n=int(input("enter the number of elements: "))
array=[]
i=0
while i<n:
    element = int(input("enter element:"))
    array.append(element)
    i+=1
sum=0
i=0
while i<len(array):
    sum+=array[i]
    i+=1
print("sum of all the elements:",sum)
