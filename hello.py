# Hello World!
# print("Hello World!")

# If statement
# if (5 > 2):
#     print("Five is greater than two")

# Variables

# x = 5
# y = "teo"
# print(x)
# print(y)

# x = 4
# x = "seker"
# print(x)

# x = str(3)
# y = int(3)
# z = float(3)
# print(x)
# print(y)
# print(z)

# print(type(x))
# print(type(y))

# Variable Names

# myvar = "Teo"
# my_var = "Teo"
# myVariableName = "Teo"

# Assign Multiple Values

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# Output Variables

# x = "Python "
# y = "is "
# z = "awesome!"
# print(x + y + z)

# x = 5
# y = "teo"
# print(x, y)

# Global Variables

x = "awesome"

def myfunc() : 
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

y = "awesome"

def myOtherFunc() :
    global y
    y = "fantastic"

myOtherFunc()

print("Python is " + y)