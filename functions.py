FILEPATH = "items.txt"


def get_todos(filepath="items.txt"):
    """ Read a text file and return the list of the to-do items  """
    with open(filepath, "r") as file_internal:
        todos_internal = file_internal.readlines()
    return todos_internal


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in a text file """
    with open(filepath, "w") as file_internal:
        file_internal.writelines(todos_arg)


if __name__ == "__main__":
    print("cicciobello")
    print(get_todos())
