import streamlit as st


st.set_page_config(page_title='Welcome, DermAIdventurers',  layout='wide', 
                   initial_sidebar_state='expanded',
                   )



st.header("Login")
# Define a username and password for login
correct_username = "user123"
correct_password = "pass123"

# Input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Initialize session_state.logged_in if not defined
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Check if login credentials are correct
if st.button("Login"):
    if username == correct_username and password == correct_password:
        st.success("Logged in as: " + username)
        st.session_state.logged_in = True
        st.write("Redirecting to the Diagnosis Page...")
        st.experimental_rerun()  
    else:
        st.error("Incorrect username or password")
        