import streamlit as st
import functions

todos=functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"]+'\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"]=""


st.title('My To-Do App')
st.write("This app is to increase your productivity")

for item in todos:
    st.checkbox(item)

st.text_input(label='',placeholder='Enter new todo...',on_change=add_todo,key='new_todo')


