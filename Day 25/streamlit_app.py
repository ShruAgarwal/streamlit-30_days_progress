import streamlit as st

st.title('st.session_state')
st.write('*The usage of Session State and Callbacks is shown in this weight conversion app!*')


with st.expander("🌟 About the app"):
     st.write("""
         Allows the implementation of session state in a Streamlit app.
         Session State is a way to share variables between reruns, for each user session. 
         In addition to the ability to store and persist state, Streamlit 
         also exposes the ability to manipulate state using Callbacks.
     """)

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)


# Another example ---->
st.header('Check how old are you!👇')

# Current year - year of Birth gives the exact age!
def age():
  st.session_state.age = 2022 - st.session_state.age

birth = st.slider('Select your year of Birth 👶', 2021, 1900, key="age")
st.button('Check my AGE', on_click = age)

st.header('Output')
st.write('st.session state', st.session_state)
