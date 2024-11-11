import streamlit as st
import pandas as pd

st.markdown(
    """
    # My First App
    Hello world :D
    """
)
 
st.title('Title: Learn Data Analysis')

st.header('Header')

st.subheader('Subheader')

st.text('Hello, future data practitioners.')

st.caption('Copyright (c) 2024')

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.dataframe(data=df, width=400, height=140)

st.table(data=df)

st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)
