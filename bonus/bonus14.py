from bonus.converters14 import convert
from bonus.parsers14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
result = round(convert(parsed['feet'], parsed['inches']), 2)

print(f"You've entered {parsed['feet']} feet and {parsed['inches']} inches")

print(f"Your Kid is {result} meters tall")
if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")

