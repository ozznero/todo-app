import random

while True:
    low_num = int(input("Enter the lower bound: "))
    high_num = int(input("Now enter the upper bound: "))
    ran_num = random.randrange(low_num, high_num + 1, 1)
    print("This is your random number: ", ran_num)
    end = input("Would you like to exit? ")
    if end == "Y":
        break
