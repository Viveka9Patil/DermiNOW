import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
import tempfile
from Add_logo import add_logo
import pandas as pd



model_file_path = r"/model.h5"
# If the model is in the same directory as the main
# you don't need to give absolute path but if it's not give the absolute path
model = tf.keras.models.load_model(model_file_path)

# So basically this over here gives the model the prediction names without this the prediction names would be
# 0,1,2,3 and so on this gives the names as you see
# The model basically predicts 0,1,2 and the probability of each then takes the highest and shows that
# I have just given 0,1,2,3 names here
class_to_condition = {
    0: "Acne and Rosacea",
    1: "Atopic Dermatitis",
    2: "Cellulitis Impetigo and other Bacterial Infections",
    3: "Eczema",
    4: "Hair Loss Alopecia and other Hair Diseases",
    5: "Light Diseases and Disorders of Pigmentation",
    6: "Lupus and other Connective Tissue Diseases",
    7: "Melanoma Skin Cancer Nevi and Moles",
}

# this function is to process the incoming image to make it fit properly inside the ML model
def preprocess_image(uploaded_image):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_image.read())
        temp_file_path = temp_file.name

    image = cv2.imread(temp_file_path)

    image = cv2.resize(image, (128, 128))

    image = image.astype(np.float32) / 255.0

    if image.shape[-1] != 3:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    image = np.expand_dims(image, axis=0)

    return image

st.set_page_config(page_title='DermiNOW!',  layout='wide', page_icon='DermiNOW.png',
                 
)
               
st.markdown(
    """
    <style>
    .stApp {
        background-color: #CEEDB6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

add_logo(logo_url = 'DermiNOW.png')





# Initialize session_state.logged_in if not defined
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Initialize session_state.user_type if not defined
if "user_type" not in st.session_state:
    st.session_state.user_type = None

# Define user types (patient and doctor)
user_types = ["Patient", "Doctor"]

# Define page list for patients
patient_pages = ["Home", "About", "Diagnosis", "Report", "Ayurveda"]

# Define page list for doctors
doctor_pages = ["Home", "About", "Diagnosis", "Report", "Biopsy", "Prescription", "Patient Monitoring"]

# Create a sidebar for navigation
page_list = patient_pages  # Default to patient pages
if st.session_state.user_type == "Doctor":
    page_list = doctor_pages

page = st.sidebar.selectbox("Select a Page", page_list)

# Define login credentials for patients and doctors
patient_credentials = {"patient123": "pass123"}
doctor_credentials = {"doctor123": "pass123"}

if page == "Home":    
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    user_type = st.selectbox("Select User Type", user_types)
    
    if st.button("Login"):
        if user_type == "Patient" and username in patient_credentials and password == patient_credentials[username]:
            st.success("Logged in as a Patient: " + username)
            st.session_state.logged_in = True
            st.session_state.user_type = "Patient"
        elif user_type == "Doctor" and username in doctor_credentials and password == doctor_credentials[username]:
            st.success("Logged in as a Doctor: " + username)
            st.session_state.logged_in = True
            st.session_state.user_type = "Doctor"
        else:
            st.error("Invalid credentials. Please try again.")

if st.session_state.logged_in:
    if st.session_state.user_type == "Patient":
        # Patient-specific content
        if page == "About":
           st.title("Welcome to DermiNOW!")
           st.header("About Us")

        # About Us content
           st.markdown(
            """
            At DermiNow, we are driven by a deep-rooted commitment to revolutionize dermatological disease diagnosis and treatment, seamlessly integrating the power of modern machine learning with the timeless wisdom of Ayurveda. Our mission is to empower individuals to take control of their skin health with a holistic approach that harmonizes the cutting-edge technology of today with the ancient, time-tested traditions of Indian medicine.

            **Bridging Science and Tradition**

            Our journey began with a vision to bridge the gap between science and tradition. Inspired by the rich heritage of Ayurveda, one of the world's oldest holistic healing systems, we have harnessed the potential of Machine Learning to create a transformative platform. It allows you to effortlessly scan or upload images of skin conditions, delivering precise and accurate diagnoses within seconds.

            **Ayurvedic Wisdom**

            What sets us apart is our commitment to Ayurvedic principles. Ayurveda, originating in ancient India, emphasizes a personalized approach to healthcare, recognizing that each individual is unique. At DermiNow, we respect this wisdom by not only providing diagnoses but also crafting customized Ayurvedic treatment plans. These plans are rooted in the belief that a balance between mind, body, and spirit is essential for radiant skin health.

            **Our Team**

            Behind our innovative platform is a passionate and multidisciplinary team dedicated to your well-being. Meet the minds driving our mission:

            - Viveka Patil

            - Lakshita Sathe

            - Rujuta Thombre

            - Anica Gupta

            - Devika Nair

            - Vagmin Yadhav

            - Dr. Sanket Bapat

            At DermiNow, we are on a mission to merge the ancient wisdom of Ayurveda with the precision of modern technology. Together, we aim to empower you with the knowledge and tools to achieve healthier, happier skin through a harmonious balance of tradition and innovation. Join us on this transformative path to skin wellness.
            """,
            unsafe_allow_html=True
        )

        elif page == "Diagnosis":
            st.header("Image Upload")
            st.write("Upload the image you want to analyze:")
            c1, c2 = st.columns(2)
            with c1:
               uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
            if uploaded_image is not None:
                st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
            st.write("You can now process this image or perform other actions.")

            with c2:
              picture = c2.camera_input("Take a picture")
            if picture:
                c2.image(picture)

        elif page == "Report":
          st.subheader("Skin Health Report")
          forms = st.form("Skin Health Form")
          with forms:
            st.markdown('<p class="medium-font">Patient Information</p>', unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            c1.text_input("Patient name")
            c2.text_input("Date of Birth")
            c3.selectbox("Gender", ("Female", "Male", "Non-Binary", "Transgender", "Other"))
            medic = c1.text_input("Select Name of Dermatologist")
            st.markdown('<p class="medium-font">Medical History</p>', unsafe_allow_html=True)
            c5, c6, c7 = st.columns(3)
            c5.text_input("Existing medical conditions that could affect skin health(Allergies)")
            c6.text_input("Previous Skin Conditions and medical treatments")
            c7.text_input("Family members with skin conditions")
            st.markdown('<p class="medium-font">Skin Type Assessment</p>', unsafe_allow_html=True)
            c8, c9 = st.columns(2)
            c8.selectbox("Skin Type", ("Combination", "Dry", "Oily"))
            c9.text_input("Skin Sensitivities/Allergies")
            st.markdown('<p class="medium-font">Skin Examination</p>', unsafe_allow_html=True)
            st.markdown('<p class="medium-font">Coloration</p>', unsafe_allow_html=True)
            c11, c12 = st.columns(2)
            c11.checkbox("Pale")
            c12.checkbox("Red")
            st.markdown('<p class="medium-font">Texture</p>', unsafe_allow_html=True)
            c13, c14, c15 = st.columns(3)
            c13.checkbox("Smooth")
            c14.checkbox("Rough")
            c15.checkbox("Scaly")
            st.markdown('<p class="medium-font">Lesions</p>', unsafe_allow_html=True)
            c16, c17, c18 = st.columns(3)
            c16.checkbox("Moles")
            c17.checkbox("Warts")
            c18.checkbox("Acne")
            c16.checkbox("Rashes/Eruptions")
            c17.checkbox("Itching/Discomfort")
            c18.checkbox("Splinters")
            c16.multiselect("Location of Skin Issues", ("Face", "Neck", "Arms", "Back"))
            st.markdown('<p class="medium-font">Skin Care Routine</p>', unsafe_allow_html=True)
            c19, c20, c21 = st.columns(3)
            c19.text_input("Moisturizer")
            c20.text_input("Cleanser")
            c21.text_input("Serum")
            c19.text_input("Sunscreen")
            st.markdown('<p class="medium-font">Medication and Treatment</p>', unsafe_allow_html=True)
            c22, c23, c24 = st.columns(3)
            c22.text_input("Medication")
            c23.multiselect("Route of Administration", ("IV", 'Oral', "IM"))
            c24.text_input("Dosage of Medication")

          st.form_submit_button("Save and Submit")

          st.button("Share ✉️")

        elif page == "Ayurveda":
           st.header("Ayurvedic Skin Recommendations")
           st.write("Answer a few questions to receive personalized Ayurvedic recommendations for your skin health.")
         # Add Ayurvedic recommendation questions and logic here

         # Your Recommendation System code
           doctors_data = [
            {"name": "Dr. Mahesh Singh", "area": "Pune"},
            {"name": "Dr. Deepak Chopra", "area": "Mumbai"},
            {"name": "Dr. Lisa Davis", "area": "Kerala"},
            ]

           medication_data = {
            "Eczema": ["Eladi Keram: Eladi Keram is an Ayurvedic remedy for eczema used to treat skin conditions like pigmentation and blemishes. Through topical use, its various ingredients support optimum skin health. Rashes, itching, and skin allergies can also be treated with Eladi Keram. It also works as an antibacterial and Ayurvedic blemish treatment remedy to address skin conditions brought on by toxins buildup. Skin disorders caused by vitiated Vata and Kapha Doshas can be treated with Eladi Keram.", "Manjishtadi kwath: Manjishtadi kwath is beneficial for treating skin concerns as well as can help purify the blood. The kwath's anti-inflammatory capabilities and ability to reduce discomfort can help with symptoms, plus maintain natural complexion and manages uneven skin tone. It is a superb detoxifier made with organic herbs and aids in systemic blood filtration. It is also a viable Ayurvedic treatment option for conditions like acne and eczema."],
            "Ring Worm": ["Ayurvedic Treatment C", "Ayurvedic Treatment D"],
            "Melanoma": ["Ayurvedic Treatment E", "Ayurvedic Treatment F"],
          }

           st.title("Doctor and Medication Recommendation System")

           disease = st.text_input("Enter the name of the disease:")

           area = st.text_input("Enter your area or location:")

        # Doctor recommendation
           st.subheader("Recommended Doctors:")
           if disease and area:
              recommended_doctors = [doctor for doctor in doctors_data if doctor["area"].lower() == area.lower()]
              if recommended_doctors:
                st.write("Doctors available in your area:")
                for doctor in recommended_doctors:
                    st.write(doctor["name"])
              else:
               st.write("No doctors found in your area for the given disease.")

        # Medication recommendation
           st.subheader("Ayurvedic Medication Recommendation:")
           if disease:
             if disease in medication_data:
                st.write(f"Ayurvedic treatments for {disease}:")
                for treatment in medication_data[disease]:
                    st.write(treatment)
             else:
                st.write("No Ayurvedic treatments found for the given disease.")
    elif st.session_state.user_type == "Doctor":
        # Doctor-specific content
        if page == "About":
            st.title("Welcome to DermiNOW!")
            st.header("About Us")

        # About Us content
            st.markdown(
            """
            At DermiNow, we are driven by a deep-rooted commitment to revolutionize dermatological disease diagnosis and treatment, seamlessly integrating the power of modern machine learning with the timeless wisdom of Ayurveda. Our mission is to empower individuals to take control of their skin health with a holistic approach that harmonizes the cutting-edge technology of today with the ancient, time-tested traditions of Indian medicine.

            **Bridging Science and Tradition**

            Our journey began with a vision to bridge the gap between science and tradition. Inspired by the rich heritage of Ayurveda, one of the world's oldest holistic healing systems, we have harnessed the potential of Machine Learning to create a transformative platform. It allows you to effortlessly scan or upload images of skin conditions, delivering precise and accurate diagnoses within seconds.

            **Ayurvedic Wisdom**

            What sets us apart is our commitment to Ayurvedic principles. Ayurveda, originating in ancient India, emphasizes a personalized approach to healthcare, recognizing that each individual is unique. At DermiNow, we respect this wisdom by not only providing diagnoses but also crafting customized Ayurvedic treatment plans. These plans are rooted in the belief that a balance between mind, body, and spirit is essential for radiant skin health.

            **Our Team**

            Behind our innovative platform is a passionate and multidisciplinary team dedicated to your well-being. Meet the minds driving our mission:

            - Viveka Patil

            - Lakshita Sathe

            - Rujuta Thombre

            - Anica Gupta

            - Devika Nair

            - Vagmin Yadhav

            - Dr. Sanket Bapat

            At DermiNow, we are on a mission to merge the ancient wisdom of Ayurveda with the precision of modern technology. Together, we aim to empower you with the knowledge and tools to achieve healthier, happier skin through a harmonious balance of tradition and innovation. Join us on this transformative path to skin wellness.
            """,
            unsafe_allow_html=True
        )
            # Add content here

        elif page == "Diagnosis":
            st.header("Image Upload")
            st.write("Upload the image you want to analyze:")
            c1, c2 = st.columns(2)
            with c1:
              uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
            if uploaded_image is not None:
                st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
                st.write("You can now process this image or perform other actions.")

            with c2:
              picture = c2.camera_input("Take a picture")
            if picture:
                c2.image(picture)
        elif page == "Report":
            # Doctor-Patient Communication Platform
                def main():
                 st.title("Communication Platform for Doctor and Patient")

    
                 if st.button("Contact Support"):
        
                  with st.form(key='contact_support_form'):
                   st.header("Contact Support")
                   st.write("Use this form to send us a message or ask for support.")
                   message = st.text_area("Your Message", height=100)
                   submit_button = st.form_submit_button("Save and Submit",message)

       
                  if submit_button:
                    st.success("Message sent successfully!")

                if __name__ == "__main__":
                  main()

        elif page == "Biopsy":
            st.subheader("Biopsy Image Analysis")
            st.write("Upload or take a biopsy image here as a doctor.")
            c1, c2 = st.columns(2)
            with c1:
              uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
            if uploaded_image is not None:
                st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
                st.write("You can now process this image or perform other actions.")

            with c2:
              picture = c2.camera_input("Take a picture")
            if picture:
                c2.image(picture)
            

        elif page == "Prescription":
            st.subheader("Prescription Drugs")
            st.write("Input the diagnosis and get prescriptions of actual drugs here as a doctor.")
            c1 ,c2 = st.columns(2)
            c1.text_input("Enter name of the disese")
            c2.text_input("Enter the prescription drug")
            c1.button("Save and Submit")

        elif page == "Patient Monitoring":
            st.subheader("Patient Health Monitoring") 

            df = pd.read_csv("mock_data.csv")
            st.table(df)

    else:

        st.warning("Please log in to access the app.")

