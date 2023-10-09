# To-Do Manager
# now including saving item to a file

while True:
    print()
    print("To-Do Manager - choose one of the following actions...")
    user_action = input("add, list , edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("add a todo: ") + "\n"

            file = open("items.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)
            file = open("items.txt", "w")
            file.writelines(todos)
            file.close()
        case "list":
            file = open("items.txt", "r")
            todos = file.readlines()
            file.close()

            new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}. {item}")
        case "edit":
            todo_number = int(input("Enter the number of the todo to edit: "))
            todo_number = todo_number - 1
            new_todo = input("Enter the new todo: ")

            file = open("items.txt", "r")
            todos = file.readlines()
            file.close()

            file = open("items.txt", "w")
            todos[todo_number] = new_todo + "\n"
            file.writelines(todos)
            file.close()

            print("editing complete.")
            print("this is the new list of items: ")
            new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(new_todos):
                print(f"{index + 1}. {item}")
        case "complete":

            todo_number = int(input("Enter the number of the todo you want to complete: "))
            todo_number = todo_number - 1

            file = open("items.txt", "r")
            todos = file.readlines()
            file.close()

            todos.pop(todo_number)

            file = open("items.txt", "w")
            file.writelines(todos)
            file.close()

            print("this is the new list of items: ")
            new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(new_todos):
                print(f"{index + 1}. {item}")
        case "exit":
            print()
            print()
            print("thanks for using To-Do Manager... bye bye")
            break
