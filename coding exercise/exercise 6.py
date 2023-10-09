filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for filename in filenames:
    file = open(filename, "w")
    text = "Hello"
    file.write(text)
    file.close()

    