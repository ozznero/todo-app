import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("A webapp for helping people remember and prioritize tasks")
st.text("Just another website construction kit, this is streamlit on python")

for todo in todos:
    st.checkbox(todo)

st.text_input("", placeholder="Insert a new todo item")