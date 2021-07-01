# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
#
# thistuple = ("apple",)
# print(type(thistuple))
#
# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))
#
# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)
#
# # Convert the tuple into a list to be able to change it:
#
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
#
# print(x)
#
# # tuples are immutable:
# thistuple = ("apple", "banana", "cherry")
# thistuple.append("orange") # This will raise an error
# print(thistuple)

# Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

new_tuple = thistuple*2
print(new_tuple.count("orange"))
print(new_tuple.index("orange"))