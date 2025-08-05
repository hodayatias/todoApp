import functions
import time

now=time.strftime("%b %d, %Y %H:%M:%S")
print(now)
print("it is ",now)

while True:
    action=input("Type add, show, edit, complete or exit:").strip()
    if action.startswith("add"):
        todo=action[4:]+"\n"

        todos=functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif action.startswith("show"):
        todos=functions.get_todos()

        for index,item in enumerate(todos):
            print(f"{index+1}-{item.capitalize().strip("\n")}")

    elif action.startswith("edit"):
        try:
            number=int(action[5:])-1
            todos=functions.get_todos()
            todo=input("Enter a to do:")+"\n"
            todos[number]=todo
            functions.write_todos(todos)

        except ValueError|IndexError:
            print ("your command is invalid")
            continue


    elif action.startswith("complete"):
        try:
            remove=int(action[8:])
            todos=functions.get_todos()
            todos.pop(remove-1)
            functions.write_todos(todos)

        except ValueError|IndexError:
            print ("your command is invalid")
            continue


    elif action.startswith("exit"):
        break

    else: print("command invalid")

