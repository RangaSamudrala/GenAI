import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello Streamlit")

df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
st.write(df1)

c_data = pd.DataFrame(np.random.randn(50, 3), columns=['a', 'b', 'c'])
st.line_chart(c_data)