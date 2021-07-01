# # the list constructor
#
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)
#
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])
# print(thislist[-4:-1])
#
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)
#
# for x in range(3):
#     print(thislist[x])
#
# [print(x) for x in thislist]
#
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i += 1
#
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)
#
# with list comprehension:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# newlist = [x for x in fruits if "a" in x]
#
# print(newlist)
#
# def myfunc(n):
#   return abs(n - 50)
#
# thislist = [100, 50, 65, 82, 23]
#
# thislist.sort(key = myfunc)
# print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)