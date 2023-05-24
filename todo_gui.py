import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

# Create GUI elements
clock = sg.Text('', key='clock')  # Text element to display clock
label = sg.Text("Type in a to-do")  # Label for input box
input_box = sg.InputText(tooltip="Enter todo", key="todo")  # Input box for entering todo
add_button = sg.Button("Add", size=10)  # Button to add todo

list_box = sg.Listbox(values=functions._todos(), key='todos',  # List box to display todos
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")  # Button to edit selected todo
complete_button = sg.Button("Complete")  # Button to complete selected todo
exit_button = sg.Button("Exit")  # Button to exit the application

# Create the main window layout
layout = [[clock], [label], [input_box, add_button],
          [list_box, edit_button, complete_button], [exit_button]]
window = sg.Window('To-Do App', layout, font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))  # Update clock value

    if event == "Add":
        new_todo = values['todo'] + "\n"  # Get new todo from input box
        todos = functions._todos()  # Get current todos
        todos.append(new_todo)  # Add new todo to the list
        functions._todos(todos)  # Update todos in the file
        window['todos'].update(values=todos)  # Update list box with new todos

    elif event == "Edit":
        try:
            selected_indexes = window['todos'].GetIndexes()  # Get selected indexes
            new_todo = values['todo']  # Get modified todo from input box

            todos = functions._todos()  # Get current todos
            for index in selected_indexes:
                if 0 <= index < len(todos):
                    todos[index] = new_todo.strip() + "\n"  # Update selected todo
                else:
                    sg.popup("Please select valid item(s).", font=("Helvetica", 20))
                    break

            functions._todos(todos)  # Update todos in the file
            window['todos'].update(values=todos)  # Update list box with modified todos
        except IndexError:
            sg.popup("Please select item(s) to edit.", font=("Helvetica", 20))

    elif event == "Complete":
        try:
            todo_to_complete = values['todos'][0]  # Get the first selected todo
            todos = functions._todos()  # Get current todos
            todos.remove(todo_to_complete)  # Remove selected todo from the list
            functions._todos(todos)  # Update todos in the file
            window['todos'].update(values=todos)  # Update list box with updated todos
            window['todo'].update(value='')  # Clear input box
        except IndexError:
            sg.popup("Please select an item first.", font=("Helvetica", 20))

window.close()
