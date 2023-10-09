# password complexity checker
# it checks if the password is > 8 char, contains a capital letter, contains a digit
#
# this is my answer, and it works
# password = input("Insert the new password: ")
#
# if len(password) > 8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
#    print("Strong password")
# else:
#    print("weak password")


#  this is the version of Ardit; firs version storing in a list, second version storing in a dictionary
password = input("Enter the new password: ")
result = {}
if len(password) >= 8:
    result["password"] = True
else:
    result["password"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["uppercase"] = uppercase

if all(result.values()):
    print("Strong password")
else:
    print("Weak password")
