files = ["a.txt", "b.txt", "c.txt"]
for file in files:
    data = open(file, "r")
    print(data.read())
    data.close()