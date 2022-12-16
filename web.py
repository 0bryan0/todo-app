import streamlit as st
import todo_functions as functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a new todo...")
