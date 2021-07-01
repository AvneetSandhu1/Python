# # Python program showing how to use
# # string modulo operator(%) to print
# # fancier output
#
# # print integer and float value
# print("Geeks :%3d, Portal :%5.2f" % (1.76, 15.333))

# # print integer value
# print("Total students : %3d, Boys : %1d" % (240, 120))
#
# # print octal value
# print("x=%4.3o" % (25))
#
# # print exponential value
# print("%11.3E" % (356.08977))

# # try to use %d
# print("%d" %(500))

# # try to use %f
# print("x=%7.2f" %(4.66666))

# # try to use %s
# bowling_scores = [190, 135, 110, 95, 195]
# name = "Ross"
# strScores = "%s's bowling scores were %s" % (name, bowling_scores)
# print(strScores)

# # unsigned integer(%u) and integer (%i):
# print("%u" % -2000)


# # try to use format method:
# # show format () is used in dictionary
# tab = {'Vishesh': 4127, 'for': 4098, 'python': 8637678}
# # using format() in dictionary
# print('\nVishesh: {0[Vishesh]}; For: {0[for]}; '
# 'python: {0[python]}'.format(tab))
#
# print('\nVishesh: {a[Vishesh]}; For: {a[for]}; '
# 'python: {a[python]}'.format(a=tab))
#
# data = dict(fun ="VisheshforPython", adj ="Python")
# # using format() in dictionary
# print("I love {fun} computer {adj}".format(**data))

# print("I love {fun} computer {adj}".format_map(data))
#
# snack = "{1} and {0}".format("burger", "fries")
# print("\nReplaced {}".format(snack))
#
# dic = { 'fruit': 'apple', 'place':'table' }
# print("I have one %(fruit)s on the %(place)s." % dic)
#
#
# # try to use string method:
# # format a output using string() method
# cstr = "I love python"
# # Printing the center aligned
# # string with fillchr
# print("Center aligned string with fillchr: ")
# print(cstr.center(40, '$'))
# # Printing the left aligned string with "-" padding
# print("The left aligned string is : ")
# print(cstr.ljust(40, '-'))
# # Printing the right aligned string with "-" padding
# print("The right aligned string is : ")
# print(cstr.rjust(40, '-'))
#
# a = ['how', 'you', 'are', 'Hello']
# print("{0[3]}, {0[0]} {0[2]} {0[1]}?" .format(a))
#
# print("{b[3]}, {b[0]} {b[2]} {b[1]}?" .format(b = a))
#
# a = {"d":"foo", "e":"bar", "c":"baz"}
# print("{d}, {c}" .format(**a))

# input:
str = input("Enter your input here: ")
print("Input entered is: ", str)
