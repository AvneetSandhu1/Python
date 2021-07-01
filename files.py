f = open("new_file.txt", "w")
f.write("Whoops!! I deleted everything!!")

f.close()
f = open("new_file.txt", "r")
print(f.read())
f.close()