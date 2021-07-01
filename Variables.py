x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

y = "the best"
def myfunc2():
  global y
  y = "superb"

myfunc2()

print("Python is " + y)

# Unpack a list:
fruits = ["banana", "apple", "cherry"]
x, y, z = fruits
print("x is: {}\ny is: {}\nz is:{}".format(x, y, z))