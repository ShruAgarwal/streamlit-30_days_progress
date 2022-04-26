import streamlit as st
import requests

st.title('🏀 Bored API app')

# Accept user input on the activity type by means of the st.selectbox command
st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["", "education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])


#The selected activity mentioned above is then appended to the URL via an f-string, 
# which is then used to retrieve the resulting JSON data
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()


# Displays information about the app and the JSON data via the st.expander command
c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)


# Displays a suggested activity like so ---
st.header('Suggested activity')
st.info(suggested_activity['activity'])


# Displaying the accompanying information of the suggested activity such as ---
# the Number of Participants, Type of Activity and Price
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')