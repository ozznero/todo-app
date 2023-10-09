# a simply journal app
# it asks the date, a grade for the mood and what about your thoughts flow
# for each day it creates a single file inside the journal folder
date = input("Enter today's date: ")
mood_rate = input("How do you rate your mood today, from 1 to 10?: ")
thoughts = input("Enter your thoughts flow: \n")
path = f"../journal/{date}.txt"
with open(path,"w") as file:
    row = f"Mood: {mood_rate} 3*\nThoughts: {thoughts}"
    file.writelines(row)

with open(path) as file:
    print(file.readlines())