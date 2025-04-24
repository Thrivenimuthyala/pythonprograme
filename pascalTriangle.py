# #pascal by farmula
# x=int(input("enter x value:"))
# y=int(input("enter y value:"))
# n=int(input("enter n value:"))
# print((x+y)**n)
# pascal by *'s
def pascal_triangle(n):
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        for j in range(i + 1):
            print('* ', end='')
        print()
rows = 5
pascal_triangle(rows)
