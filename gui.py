import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter a to-do', key='todo')
add_button = sg.Button('Add')
listbox = sg.Listbox(values=functions.get_todos(),key='todos',
                     enable_events=True, size=(45,10))
edit_button = sg.Button('Edit')

window=sg.Window('My To-Do App',
                 layout = [[label], [input_box, add_button], [listbox, edit_button]],
                 font = ('Helvetica', 15))
while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo']+'\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_remove=values['todos'][0]
            new_todo = values['todo']+'\n'
            todos=functions.get_todos()
            index=todos.index(todo_to_remove)
            todos[index]=new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()

