# To-Do Manager
# now including saving item to a file
# v5 new check in the user_action, this time verifies if the action is at the beginning of the input
# also introduces error handling and custom functions
# --> placed the custom function in the functions.py file
import time
from functions import get_todos, write_todos

barzelletta = """
Un daino incontra un altro daino, e gli dice:
    - giochiamo a nascon-daino?
e l'altro daino:
    - dai, no
"""
adesso = time.strftime("Oggi è %A %d %b %Y, sono le %H:%M e %S secondi")
print("\nBenvenuti! ", adesso)

while True:
    print("\nTo-Do Manager - choose one of the following actions...")
    user_action = input("add, list , edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith("list"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            todo_number = int(user_action[5:])
            todo_number = todo_number - 1

            todos = get_todos()

            check = todos[todo_number]
            new_todo = input("Enter the new todo: ")
            todos[todo_number] = new_todo + "\n"

            write_todos(todos)

            print("editing complete.")
            print("this is the new list of items: ")
            new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(new_todos):
                print(f"{index + 1}. {item}")
        except IndexError:
            print("There's no item associated to the number you specify")
            continue
        except ValueError:
            print("You have to specify which number you want to edit")
            continue
    elif user_action.startswith("complete"):
        try:
            todo_number = int(user_action[9:])
            todo_number = todo_number - 1

            todos = get_todos()

            removing = todos[todo_number].strip("\n")

            todos.pop(todo_number)

            write_todos(todos)

            print(f"{removing} removed from the to-do list \n")
            time.sleep(1)

            print("this is the new list of items: ")
            new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(new_todos):
                print(f"{index + 1}. {item}")
        except IndexError:
            print("There's no item associated to the number you specify")
            continue
        except ValueError:
            print("You have to specify which number you want to complete")
            continue
    elif user_action.startswith("exit"):
        print()
        print()
        print("thanks for using To-Do Manager... bye bye")
        break
    elif user_action.startswith("barz"):
        print(barzelletta)
    else:
        print("You have inserted an invalid command. Retry")
        time.sleep(1)

# end :)
