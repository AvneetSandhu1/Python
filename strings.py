# txt = "The best things in life are free!"
# print("expensive" not in txt)
# print("expensive" in txt)
#
# # string slicing:
# b = "Hello, World!"
# print(b[2:5])
#
# # negative slicing:
# print(b[-5:-2])
#
# # reverse the string:
# print(b[::-1])
#
# # jumps of 2, print from 1st to 5th character:
# print(b[1:6:2])
#
# # case change:
# print(b.upper())
# print(b.lower())
# print(b.strip("H"))
# print(b.replace("H", "J"))
# print(b.split())
# print(b.split(','))
#
# b = 'where are you?'
# print(b.title())
# print(b.capitalize())
# print(b.istitle())
#
# # returning a string in the center with specified padding around it.
# print(b.center(20,"$"))
#
# print(b.count("e"))
# e = "Hello thERe!"
# print(e.casefold())
#
# # string encoding and decoding:
# Str = b'\xd7\xa9\xd7\x9c\xd7\x95\xd7\x9d'
# x = Str.decode()
# print(x)
# y = x.encode()
# print(y)
#
# text = "Python is easy to learn."
#
# result = text.endswith('to learn')
# # returns False
# print(result)
#
# result = text.endswith('to learn.')
# # returns True
# print(result)
#
# text = "Python programming is easy to learn."
#
# # start parameter: 7
# # "programming is easy to learn." string is searched
# result = text.endswith('learn.', 7)
# print(result)
#
# # Both start and end is provided
# # start: 7, end: 26
# # "programming is easy" string is searched
#
# result = text.endswith('is', 7, 26)
# # Returns False
# print(result)
#
# result = text.endswith('easy', 7, 26)
# # returns True
# print(result)

# str.isdecimal() (Only Decimal Numbers)
# str.isdigit() (Decimals, Subscripts, Superscripts)
# str.isnumeric() (Decimals, Subscripts, Superscripts, Vulgar Fractions, Roman Numerals, Currency Numerators)
# a = "32"
# print("32 is a decimal: ", a.isdecimal())
# print("32 is a digit: ", a.isdigit())
# print("32 is a numeric: ", a.isnumeric())
#
# a = "\u00B2"
# print(a, " is a decimal: ", a.isdecimal())
# print(a, " is a digit: ", a.isdigit())
# print(a, " is a numeric: ", a.isnumeric())
#
# a = "\u00BC"
# print(a, " is a decimal: ", a.isdecimal())
# print(a, " is a digit: ", a.isdigit())
# print(a, " is a numeric: ", a.isnumeric())
#
# random_string = '   this is good '
#
# # Leading whitepsace are removed
# print(random_string.lstrip())
#
# # Argument doesn't contain space
# # No characters are removed.
# print(random_string.lstrip('sti'))
# print(random_string.lstrip('s ti'))
#
# website = 'https://www.programiz.com/'
# print(website.lstrip('htps:/.'))
#
# # .join() with lists
# numList = ['1', '2', '3', '4']
# separator = '+'
# print(separator.join(numList))
#
# # .join() with tuples
# numTuple = ('1', '2', '3', '4')
# print(separator.join(numTuple))
#
# txt = "Good night Sam!"
# x = "mSa"
# y = "eJo"
# z = "odnght"
# mytable = txt.maketrans(x, y, z)
# print('mytable is: ', mytable)
# print(txt.translate(mytable))
#
# my_string = "    "
# print(my_string.isspace())
str = "Woohoo!"
print(str.ljust(20,"!"))

print(bool("abcdef"))