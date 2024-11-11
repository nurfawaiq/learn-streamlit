import streamlit as st
 
name = st.text_input(label='Name', value='')
st.write('Name : ', name)

text = st.text_area('Address')
st.write('Address : ', text)

number = st.number_input(label='Age')
st.write('Age : ', int(number), ' y.o')

import datetime

date = st.date_input(label='Date of Birth', min_value=datetime.date(1900, 1, 1))
st.write('Date of Birth :', date)

import pandas as pd
 
uploaded_file = st.file_uploader('Choose a CSV file')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)

if st.button('Say hello'):
    st.write('Hello there')

agree = st.checkbox('I agree')
if agree:
    st.write('Welcome to MyApp')

genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)
