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

# x = "awesome"

# def myfunc() : 
#     x = "fantastic"
#     print("Python is " + x)

# myfunc()

# print("Python is " + x)

# y = "awesome"

# def myOtherFunc() :
#     global y
#     y = "fantastic"

# myOtherFunc()

# print("Python is " + y)

# Numbers

# x = 1
# y = 2.8  
# z = 1j

# print(type(x))
# print(type(y))
# print(type(z))

# a = float(x)
# b = int(y)
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

# import random

# print(random.randrange(1, 10))

# Strings

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
# print(a[1])

# for x in "banana":
#   print(x)

# print(len(a))

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# b = "Hello World!"
# print(b[2:5])
# print(b[:5])
# print(b[2:])
# print(b[-5: -2])

# print(b.upper())
# print(b.lower())

# a = " Hello, World! "
# print(a.strip())
# print(a.replace("H", "J"))
# print(a.split(","))

# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# Booleans

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


print(bool("Hello"))
print(bool(15))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")