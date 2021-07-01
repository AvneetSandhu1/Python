thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#
# print(thisdict)
# print(type(thisdict))
#
# # accessing the key values:
# print(thisdict["colors"])
# print(thisdict.get("colors"))
#
# # get all the keys in dict:
# x = thisdict.keys()
# print(x)
# for k in x:
#     print(k, ": ", thisdict[k])
#
# # add a key to the dictionary:
# thisdict["fuel"] = "Diesel"
# print(x)
#
# # get all the values and items:
# y = thisdict.values()
# print(y)
# z = thisdict.items()
# print(z)
#
# # change one of the values:
# thisdict["fuel"] = "Petrol"
# print(y)
# print(z)
#
# # update the value:
# thisdict.update({"fuel": "Diesel"})
# print(z)
#
# # remove a pair:
# thisdict.pop("fuel")
# print(z)
#
# thisdict["fuel"] = "Diesel"
# print(thisdict.popitem())
#
# z = thisdict.items()
# thisdict["fuel"] = "Diesel"
# print(z)
# del thisdict["fuel"]
# print(z)
#
# # del thisdict
# # print(thisdict)
#
# thisdict.clear()
# print(z)

# print keys:
# for x in thisdict:
#     print(x)
# for x in thisdict.keys():
#     print(x)
#
# print values:
# for x in thisdict:
#     print(thisdict[x])
#
# for x in thisdict.values():
#     print(x)
#
# # print items:
# for x in thisdict.items():
#     print(x)
#
# mydict = thisdict.copy()
# print(mydict)
#
# del mydict
# mydict = dict(thisdict)
# print(mydict)

# nested dictionaries:
nest_dict = {"child1": {
    "name": "Kierath",
    "age": 9},
    "child2": {
    "name": "Maahi",
    "age": 6
}}

print(nest_dict)

# or create three dictionaries ad assign those in nested one:
child1 = {
    "name": "Kierath",
    "age": 9}

child2 = {
    "name": "Maahi",
    "age": 6}

new = {"child1": child1, "child2": child2}
print(new)