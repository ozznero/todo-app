filenames = ["1.doc", "2.report", "3.presentation"]

filenames = [file.replace(".", "-", 1) + ".txt" for file in filenames]

print(filenames)
# for file in filenames:
  # print(file.replace(".","-", 1))
