import streamlit as st
import pandas as pd

st.title("Streamlit Widgets Example")
st.write("This is a simple Streamlit app with various widgets.")

# Text input
name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")


age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")

options = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {options}")
st.write("This is a simple text area:")
text = st.text_area("Enter some text:")
st.write(f"You entered: {text}")

# file uploader
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
if uploaded_file is not None:
    # Read the file and display its contents
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        st.write("CSV file contents:")
        st.dataframe(df)
    else:
        content = uploaded_file.read().decode("utf-8")
        st.write("Text file contents:")
        st.text(content)