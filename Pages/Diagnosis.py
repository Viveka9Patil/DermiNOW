import streamlit as st


st.set_page_config(page_title='DermAIdventurers',  layout='wide', 
                   initial_sidebar_state='expanded',
                   )

st.header("About Dermatology")
st.write("Dermatology is the branch of medicine that deals with the skin, hair, nails, and related disorders.")
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
