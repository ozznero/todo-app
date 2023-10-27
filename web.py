import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("A webapp for helping people remember tasks")
st.text("streamlit - Just another website construction kit")

for todo in todos:
    st.checkbox(todo)

st.text_input(" ", placeholder="Insert a new todo item",
              on_change=add_todo, key='new_todo')

print("New roundtrip")
st.session_state