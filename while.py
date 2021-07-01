i = 1
while i < 6:
    if i == 3:
        print("skipping 3")
        i += 1
        continue
    print(i)
    i += 1
    if i == 5:
        print("stopping first loop at 4!")
        break

while i < 8:
    print(i)
    i += 1
else:
    print("stopped at 8!")