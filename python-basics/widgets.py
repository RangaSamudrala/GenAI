import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlist Text Input")

name = st.text_input("Enter name: ")

if name:
	st.write(f"Hello {name}")

age = st.slider("Select age: ", 0, 100, 10)

st.write(f"Age is: {age}")
