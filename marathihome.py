import streamlit as st

# Define a username and password for login
correct_username = "user123"
correct_password = "pass123"

# Streamlit app title with custom style
st.title("डर्मॅटोलॉजी एआय डायग्नोस्टिक्स")
st.markdown("---")

# Initialize session_state.logged_in if not defined
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Initialize selected_tab
selected_tab = None

# Sidebar for login with custom style
st.sidebar.title("मेनू")
st.sidebar.markdown("---")

# Check if the user is already logged in
if st.session_state.logged_in:
    # Display "Log Out" button when logged in
    if st.sidebar.button("लॉग आउट", key="log_out_button"):
        st.session_state.logged_in = False
        st.sidebar.warning("लॉग आउट. कृपया पुन्हा लॉग इन करण्यासाठी पुन्हा लॉग इन करा.")
else:
    # Display login fields if the user is not logged in
    username = st.sidebar.text_input("वापरकर्तानाव")
    password = st.sidebar.text_input("संकेतशब्द", type="password")

    # Display "लॉग इन" button with custom style when not logged in
    if st.sidebar.button("लॉग इन", key="log_in_button"):
        if username == correct_username and password == correct_password:
            st.sidebar.success("वापरकर्तानाव: " + username)
            st.session_state.logged_in = True
        else:
            st.sidebar.error("चुकीचे वापरकर्तानाव किंवा संकेतशब्द")
            st.session_state.logged_in = False

# Add custom CSS to style the app
st.markdown(
    """
    <style>
    /* Add your custom CSS styles here */
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
    }
    .st-title {
        font-size: 36px;
        color: #333;
    }
    .st-markdown {
        font-size: 18px;
        color: #555;
    }
    .st-sidebar {
        background-color: #333;
        color: #fff;
    }
    .st-button {
        background-color: #0074e4;
        color: #fff;
        font-weight: bold;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display content based on the selected tab
if st.session_state.logged_in:
    selected_tab = st.sidebar.radio("एक पृष्ठ निवडा:", ["मुख्यपृष्ठ", "डर्मॅटोलॉजी बद्दल", "छवी अपलोड"])

if not st.session_state.logged_in:
    st.sidebar.warning("कृपया वापरकर्तानावसाठी लॉग इन करा.")

if selected_tab == "मुख्यपृष्ठ":
    st.header("डर्मॅटोलॉजी एआय डायग्नोस्टिक्समध्ये स्वागत आहे")
    st.write("हा मुख्यपृष्ठ आहे.")

elif selected_tab == "डर्मॅटोलॉजी बद्दल":
    st.header("डर्मॅटोलॉजी बद्दल")
    st.write("डर्मॅटोलॉजी ही त्वचा, केस, नाखुळे आणि संबंधित अशा विकारांसह संबंधित विचार करणारी वैद्यकीय शाखा आहे.")

elif selected_tab == "छवी अपलोड":
    st.header("छवी अपलोड")
    st.write("आपल्याला विचारल्याची छवी अपलोड करा:")
    c1, c2 = st.columns(2)
    with c1:
      uploaded_image = st.file_uploader("छवी निवडा...", type=["jpg", "png", "jpeg"])
      if uploaded_image is not None:
        st.image(uploaded_image, caption="अपलोड केलेली छवी", use_column_width=True)
      st.write("आपण आत्ताच या छवीचा प्रक्रिया करू शकता किंवा इतर क्रियाओं करू शकता.")

    with c2:
     picture = c2.camera_input("फोटो घेण्याची क्रिया")
     if picture:
        c2.image(picture)
