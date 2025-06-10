# # 1 write a program that prompts the user for two numbers and displays the addition , subtraction, multiplication, and division between them
# num1=int(input("enter num1 value: "))
# num2=int(input("enter num2 value: "))
# addition=num1+num2
# subtraction=num1-num2
# multiplication=num1*num2
# division=num1/num2
# print("addition of two number: ",addition)
# print("subtraction of two number: ",subtraction)
# print("multiplication of two number: ",multiplication)
# print("division of two number: ",division)
# # 2 write a program that calculates the arithmetic mean of two numbers
# num1=float(input("enter num1 value: "))
# num2=(float(input("enter num2 value: ")))
# arithmetic_mean=(num1+num2)/2
# print("the arithmetic mean is: ",arithmetic_mean)
# # 3 create a program that calculates and displays the arithmetic mean of three grades by the user.
# grade1=float(input("enter first grade: "))
# grade2=float(input("enter second grade: "))
# grade3=float(input("enter third grade: "))
# arithmetic_mean=(grade1+grade2+grade3)/3
# rounded_mean=round(arithmetic_mean,2)
# print("the arithmetic mean of grades: ",rounded_mean)
## 4 write a program that calculates the geometric mean of three numbers entered by the user.
# import math
# num1=float(input("enter num1 value: "))
# num2=float(input("enter num2 value: "))
# num3=float(input("enter num3 value: "))
# multi=num1*num2*num3
# GM=math.pow(multi,1/3)
# print("geometric mean is: ",GM)
# #  5 write a program that calculates the BMI of an individual, using the formula BMI=weight/height**2
# weight=float(input("enter your weight: "))
# height=float(input("enter your height: "))
# BMI=weight/(height**2)
# print("your BMI is :",BMI)
# # 6 create a program that calculates and displays the perimeter of a circle, prompting the user for the radius
# import math
# radius=float(input("enter radius of circle: "))
# parimeter_circle=2*math.pi*radius
# print("the perimeter of circle is : ",parimeter_circle)
# # 7 create a program that calculates and displays the area of a circle, prompting the user for the radius
# import math
# radius=float(input("enter radius of circle: "))
# area_circle=math.pi*radius**2
# print("the area of circle is : ",area_circle)
# #  8 write a program that calculates the delta of a quadratic equation (delta=b**2-4ac)
# a=float(input("enter the coefficient a: "))
# b=float(input("enter the coefficient b: "))
# c=float(input("enter the coefficient c: "))
# delta=b**2-4*a*c
# print("the delta of quadratic equation is :",delta)
# # 9 write a program that calculates the parimeter and area of a rectangle, using the formula
# width=float(input("enter radius of circle: "))
# length=float(input("enter radius of circle: "))
# parimeter_rectangle=2*(width+length)
# area_rectangle=width*length
# print("the parimeter of rectangle: ",parimeter_rectangle)
# print("the area of rectangle: ",area_rectangle)
# # 10 write a program that calculates the perimter and sres of a triangle, using the formulas P=a+b+c and A=(b*h)/2
# a=float(input("enter the coefficient a: "))
# b=float(input("enter the coefficient b: "))
# c=float(input("enter the coefficient c: "))
# h=float(input("enter the height: "))
# P=a+b+c
# A=(b*h)/2
# print("the parimeter : ",P)
# print("the area :",A)