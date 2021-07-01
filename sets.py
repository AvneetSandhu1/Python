# # Duplicate values will be ignored:
# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)
#
# for x in thisset:
#     print(x)
#
# # the following does not work:
# # i = 0
# # while i < len(thisset):
# #     print(thisset[i])
# #     i += 1
#
# thisset.add("orange")
# print(thisset)
#
# berries = {"strawberry", "blueberry", "raspberry"}
# thisset.update(berries)
# print(thisset)
#
# thisset.remove("raspberry")
# print(thisset)
#
# thisset.discard("strawberry")
# print(thisset)
#
# print(thisset.pop())
# print(thisset)
#
# thisset.clear()
# print(thisset)
#
# del thisset
# print(thisset)
#
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
#
# set3 = set1.union(set2)
# print(set3)
#
# set1.update(set2)
# print(set1)
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)
#
# a = z.copy()
# print(a)
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.difference(y)
# print(z)
#
# x.difference_update(y)
# print(x)
# del x
# del y
# del z
#
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.isdisjoint(y)
# print(z)
# del x
# del y
# del z
#
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

z = y.issuperset(x)
print(z)
#
# y.remove("b")
# z = x.issubset(y)
# print(z)
#
