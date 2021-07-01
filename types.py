print("45e5 is a ", type(45e5))
print(45e5)

x = 1+4j
print(x)
print(type(x))

# setting types:
x = float(1)
print(x)

x = int(35.67)
print(x)

x = list((1, 4, 6, 8, 9))
print(x)
print(type(x))

x = tuple((1, 4, 6, 8, 9))
print(x)
print(type(x))

x = dict(apple = 5, pear = 6)
print(x)
print(type(x))

x = complex(7)
print(x)
print(type(x))

x = complex(2+5)
print(x)
print(type(x))

# cant convert complex to another type:
# z = float(7 + 4j)
# print(x)
# print(type(x))