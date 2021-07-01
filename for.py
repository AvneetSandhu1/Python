# for loops with lists:
a = [1, 2, 3]
for x in a:
    print(x)
else:
    print(a)

for x in range(2, 30, 3):
    if x == 14:
        continue
    elif x == 29:
        break
    print(x)

for x in range(3):
    pass

for x in "banana":
    print(x)