todos = []

while True:
    print()
    print("To-Do Manager - choose one of the following actions...")
    action = input("add, list , edit, complete or exit: ")
    match action:
        case "add":
            todo = input("add a todo: ")
            todos.append(todo)
        case "list":
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
        case "edit":
            todo_number = int(input("Enter the number of the todo to edit: "))
            todo_number = todo_number - 1
            new_todo = input("Enter the new todo: ")
            todos[todo_number] = new_todo
            print("editing complete.")
            print("this is the new list of items: ")
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
        case "complete":
            todo_number = int(input("Enter the number of the todo you want to complete: "))
            todo_number = todo_number - 1
            todos.pop(todo_number)
            print("this is the new list of items: ")
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item}")
        case "exit":
            print()
            print()
            print("thanks for using To-Do Manager... bye bye")
            break
