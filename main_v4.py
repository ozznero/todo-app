# To-Do Manager
# now including saving item to a file
# v4 improving the add feature with IN operator and if condition
from time import sleep

while True:
    print()
    print("To-Do Manager - choose one of the following actions...")
    user_action = input("add, list , edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        todo = user_action[4:] + "\n"

        with open("items.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("items.txt", "w") as file:
            file.writelines(todos)

    elif "list" in user_action:
        with open("items.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif "edit" in user_action:
        todo_number = int(user_action[5:])
        todo_number = todo_number - 1
        new_todo = input("Enter the new todo: ")

        with open("items.txt", "r") as file:
            todos = file.readlines()

        todos[todo_number] = new_todo + "\n"

        with open("items.txt", "w") as file:
            file.writelines(todos)

        print("editing complete.")
        print("this is the new list of items: ")
        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            print(f"{index + 1}. {item}")

    elif "complete" in user_action:
        todo_number = int(user_action[9:])
        todo_number = todo_number - 1

        with open("items.txt", "r") as file:
            todos = file.readlines()

        removing = todos[todo_number].strip("\n")

        todos.pop(todo_number)

        with open("items.txt", "w") as file:
            file.writelines(todos)

        print(f"{removing} removed from the to-do list \n")
        sleep(1)

        print("this is the new list of items: ")
        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            print(f"{index + 1}. {item}")

    elif "exit" in user_action:
        print()
        print()
        print("thanks for using To-Do Manager... bye bye")
        break

    else:
        print("You have inserted an invalid command. Retry")
        sleep(1)

# end :)