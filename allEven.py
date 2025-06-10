n=int(input("enter how many element you to need:"))
array=[]
for i in range(0,n):
    elmt=int(input("enter the element: "))
    array.append(elmt)
print(array)
all_even=True
for elmt in array:
    if elmt%2!=0:
        all_even=False
        break
if all_even:
    print("all are even")
else:
    print("all are not even")