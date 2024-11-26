import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Set the page configuration
st.set_page_config(page_title="Biography", page_icon="🤖", layout="wide")

# Header Section
st.title("Biography 🤖")
st.write("---")

# About Me Section
st.subheader("About Me")
about_me = st.text_area(
    "About Me",
    "The baby of the family and a budding tech whiz, I'm ready to tackle the challenges of Computer Engineering at Surigao del Norte State University."
)

# Default image URL
default_image_url = "https://via.placeholder.com/400"  # Replace with your default image URL

# Image Section
st.subheader("Profile Picture")
uploaded_image = st.file_uploader("Upload Profile Picture", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    try:
        image = Image.open(uploaded_image)
        st.image(image, caption="Profile Picture", width=400)
    except Exception as e:
        st.error(f"Error displaying the uploaded image: {e}")
else:
    try:
        response = requests.get(default_image_url)
        response.raise_for_status()  # Raise an error for invalid responses
        default_image = Image.open(BytesIO(response.content))
        st.image(default_image, caption="Default Profile Picture", width=400)
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching the default image: {e}")

# Personal Information and Contact
st.header("Personal Information")
col1, col2 = st.columns(2)

with col1:
    last_name = st.text_input("Last Name:", value="Yamit")
    first_name = st.text_input("First Name:", value="Hannah Bea")
    middle_initial = st.text_input("Middle Initial:", value="M.")
    gender = st.text_input("Gender:", value="Female")
    age = st.number_input("Age:", min_value=0, value=18)

with col2:
    number = st.text_input("Number:", value="+639852273262")
    email = st.text_input("Email:", value="beayamit16@gmail.com")
    facebook = st.text_input("Facebook account:", value="Hana Yamit")
    instagram = st.text_input("Instagram account:", value="h4nn4h_prl")
    address = st.text_area("Home Address:", value="P-5 Ombong, Alegria, Surigao del Norte")

# Parents Section
st.header("Parents")
father_name = st.text_input("Father's Name:", value="Rogelio Y. Yamit")
mother_name = st.text_input("Mother's Name:", value="Thelma M. Yamit")

# Educational Attainment
st.header("Educational Attainment")
elementary = st.text_input("Elementary:", value="Ombong Elementary School")
junior_high = st.text_input("Junior High School:", value="Alegria National High School")
senior_high = st.text_input("Senior High School:", value="Alegria Stand Alone Senior High School")
