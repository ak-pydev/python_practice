import streamlit as st
import pandas as pd
import numpy as np

#Title of the app
st.title("hello streamlit")

#Display a simple text
st.write("This is a simple Streamlit app.")

#Display a dataframe
data = {
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D'],
    'Column 3': [True, False, True, False],
    'Column 4': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
st.write("Here is a sample dataframe:")
st.dataframe(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)
st.map()
