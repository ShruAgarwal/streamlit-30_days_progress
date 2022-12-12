import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('st.cache')
st.write('*Allows to optimize the performance of your Streamlit app.*')

# Using cache [EXAMPLE 1] ---->
a0 = time.time()
st.subheader('Using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time.time()
st.info(a1-a0)


# Not using cache
b0 = time.time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time.time()
st.info(b1-b0)


# [EXAMPLE 2]----> 
st.subheader('Another one using st.cache')
@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
  time.sleep(2)  # This makes the function take 2s to run
  return a * b

t = time.time()
a = 21
b = 510
res = expensive_computation(a, b)

st.write("Result:", res)
st.info(t)
