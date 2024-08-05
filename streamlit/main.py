import numpy as np
import streamlit as st
import pandas as pd

st.title("Hello")

st.write("Simple text")
st.text("Simple text")

df = pd.DataFrame({
    "first": [1, 2, 3, 4, 5],
    "second": [6, 7, 8, 9, 0]
})

st.write("dataframe")
st.write(df)


st.line_chart(pd.DataFrame(np.random.randn(20,3), columns=['a', 'b', 'c']))

st.subheader("Text Input")

name = st.text_input("Enter Name")
st.write(f"Your Name: {name}")
age = st.slider("Select age ", 0,100,25)
st.write(f"Your Age: {age}")

options = ['Python', "Java", "C++"]
choice = st.selectbox("Choose fav lang: ", options)
st.write(f"Your Selected: {choice}")



uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    file = pd.read_csv(uploaded_file)
    st.write(file)
