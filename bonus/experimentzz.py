import glob
import csv
import shutil
import webbrowser

myfiles = glob.glob("files/*.txt")

for filepath in myfiles:
    with open(filepath, "r") as file:
        print(file.read().strip())

with open("files/weather.csv","r") as file:
    data = list(csv.reader(file))

city = input("Enter a city name and you will get its temperature! : ")

for row in data:
    if row[0] == city:
        print(f"the temperature of {row[0]} is {row[1]} °C")

# shutil.make_archive("archivio","zip","files")
user_term = input("Enter a search term: ").replace(" ","+")
webbrowser.open("https://google.com/search?q="+user_term)