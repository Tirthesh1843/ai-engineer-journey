import streamlit as st

st.write("Hello World")

st.title ("tirthesh dhruv")
st.header ("header")
st.subheader ("subheader")
st.write ("write")

## Button,checkbox,radio,selectbox,slider,textarea
if st.button("button"):
    st.write("button clicked")
agree = st.checkbox("checkbox")
if agree:
    st.write("You agreed")
radio =st.radio("Gender",("Male","Female","Other"))
if radio == 'Other':
    st.text_input("Please specify your gender.")
st.selectbox("selectbox",("a","b","c"))
age = st.slider("age",10,30,18)
st.text_area("text_area")
st.write(f"Your age is {age}.")
DOB = st.date_input("Enter your date of birth")
uploaded_file = st.file_uploader("upload file", type = ["csv", "txt"])
import pandas as pd
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())