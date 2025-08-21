import streamlit as st
import numpy as np
import pandas as pd

name = st.text_input('Enter name:')
if name:
    st.write(f"hello {name}")

val = st.slider("A slider", 0, 100, 1)
if val:
    st.write(f"Slider value: {val}")

options = ['Python', 'Java', 'C++', 'Fortran']
selection = st.selectbox('Select a language:', options)
st.write(f'You selected: {selection}')
