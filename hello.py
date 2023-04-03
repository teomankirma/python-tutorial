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

# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")


# print(bool("Hello"))
# print(bool(15))

# def myFunction() :
#   return True

# if myFunction():
#   print("YES!")
# else:
#   print("NO!")

# Lists

# thisList = ["apple", "banana", "orange"]
# print(thisList)
# print(len(thisList))
# print(type(thisList))

# thisList2 = list(("apple", "banana", "orange"))
# print(thisList2)
# print(thisList2[-1])
# print(thisList[0:2])

# if "apple" in thisList2: 
#     print("Yes, 'apple' is in the fruits list.")

# thisList2[1] = "blackcurrant"
# print(thisList2)

# thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist3[1:3] = ["blackcurrant", "watermelon"]
# print(thislist3)

# thisList2[1:2] = ["blackcurrant", "watermelon"]
# print(thisList2)

# thisList[1:3] = ["watermelon"]
# print(thisList)

# thisList = ["apple", "banana", "orange"]
# thisList.insert(2, "watermelon")
# print(thisList)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# tropical = ["mango", "pinapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
# del thislist

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# Loop Lists

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# for i in range(len(thislist)):
#   print(thislist[i])

# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# [print(x) for x in thislist]

# List Cont.

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# newlist = ['hello' for x in fruits]
# print(newlist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# Tuples

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
# print(len(thistuple))

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# Sets

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# thisset.add("orange")
# print(thisset)

# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# thisset.discard("banana")
# print(thisset)

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)

# print(x)

# z = x.intersection(y)
# print(z)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)
# print(x)

# Dictionaries

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)
# print(thisdict["brand"])

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)
# thisdict.update({"country": "turkiye"})
# thisdict.update({"color": "red"})
# print(thisdict)

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily["child2"]["name"])

# If...Else

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")

# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")

# a = 33
# b = 200

# if b > a:
#   pass

# While

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")