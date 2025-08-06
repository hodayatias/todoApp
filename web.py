import streamlit as st
import functions

todos=functions.get_todos()

st.title('My To-Do App')
st.write("This app is to increase your productivity")

for item in todos:
    st.checkbox(item)

st.text_input(label='',placeholder='Enter new todo...')


