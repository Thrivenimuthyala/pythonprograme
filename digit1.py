n=int(input("enter  a digit:"))
summ=0
while(n>0):
    rem=n%10
    summ+=rem
    n=n//10
print("sum of digit is:",summ)
#product of digit
n=int(input("enter  a digit:"))
product=1
while(n>0):
    rem=n%10
    product*=rem
    n=n//10
print("sum of digit is:",product)
#count of digit
n=int(input("enter  a digit:"))
summ=0
count=0
while(n>0):
    count+=1
    n=n//10
print("count of digit is:",count)

