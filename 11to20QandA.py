# # 11 write a program that calculates the average velocity of an object, using v=s/t
# space_variation=float(input("enter the space variation : "))
# time_variation=float(input("enter the time variation : "))
# averange_velocity=space_variation/time_variation
# print("the averange velocity: ",averange_velocity)
# # 12 write a program that calculates the kinetic energy of a moving object, using the formula E=(mv**2)/2
# mass=float(input("enter the miss of an object : "))
# velocity=float(input("enter the velocity of an object : "))
# E=(mass*velocity**2)/2
# print("kinetic energy of an object: ",E)
# # 13 write a program that calculates the work done by a force actiing on an object using formula T=F*d
# force=float(input("enter the applied force :" ))
# distance=float(input("enter the distance: "  ))
# T=force*distance
# print("the work done by the object: ",T)
# # 14 write a program that calculate the distance between two points or coordinate
# X1=float(input("enter first x-coordinate : "))
# Y1=float(input("enter first y-coordinate : "))
# X2=float(input("enter second x-coordinate : "))
# Y2=float(input("enter second y-coordinate : "))
# distance=(X2-X1)**2+(Y2-Y1)**2
# print("the distance between two points: ",distance)
# # 15 write a program that calculates the volume of that sphere
# import math
# radius=float(input("enter the radius of the sphere : "))
# volume=(4/3)*math.pi*radius**3
# print("the volume of the sphere : ",volume)
# # 16 make a program that asks for a person's age and displays whether they are of legal age or not
# age=int(input("enter your  age : "))
# if age>=18:
#     print("your are legal")
# else:
#     print("your are not legal")
# # 17 write a program that reads two numbers and tells you which one is bigger
# num1=float(input("enter first number : "))
# num2=float(input("enter second number : "))
# if num1>num2:
#     print("first number is bigger")
# elif num2>num1:
#     print("second number is bigger")
# else:
# #     print("there are equal")
# # 18 write a program that reads three numbers and displays the largest one
# num1=float(input("enter first number : "))
# num2=float(input("enter second number : "))
# num3=float(input("enter third number : "))
# if num1>num2 and num1>num3:
#     print("first number is largest")
# elif num2>num1 and num2>num3:
#     print("second number is largest")
# else:
#     print("third number is largest")
# # 19 write a program that reads a number and reports whether it is odd or even
# number=int(input("enter a number : "))
# if number%2==0:
#     print("it is an even number")
# else:
#     print("it is an odd ")
# # 20 write a program that reads a number and reports whether it is positive, negative or zero
# number=int(input("enter a number : "))
# if number>0:
#     print("it is positive")
# elif number<0:
#     print("it is negative")
# else:
#     print("it is zero")