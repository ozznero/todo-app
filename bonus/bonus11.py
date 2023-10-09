def get_average():
    with open("data.txt","r") as file:
        data = file.readlines()
    values = data[1:]
    numbers = [int(number)  for number in values]
    average = sum(numbers) / len(numbers)
    return average

print("io sono groot")
print(get_average())

len()
