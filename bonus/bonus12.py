feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


parsed = parse(feet_inches)
result = round(convert(parsed['feet'], parsed['inches']),2)

print(f"You've entered {parsed['feet']} feet and {parsed['inches']} inches")

print(f"Your Kid is {result} meters tall")
if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")

