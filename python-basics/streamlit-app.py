import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello Streamlit")

st.write("This is a simple text")

df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [10, 20, 30]})

st.write("Dataframe")
st.write(df1)

chart_data1 = pd.DataFrame(np.random.randn(20, 4), columns=['a', 'b', 'c', 'd'])

st.line_chart(chart_data1)
