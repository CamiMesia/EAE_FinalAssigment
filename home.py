import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="IPLD Final Project - Natalia González",
    page_icon="👩‍💻",
    layout="centered"
)

st.title("Final Project - Introduction to Programming Languages for Data")
st.subheader("by Natalia González")

col1, col2 = st.columns([1, 2])

with col1:
    try:
        image = Image.open("natalia.jpg")  # Cambia por el nombre de tu archivo
        st.image(image, caption="Natalia González", use_column_width=True)
    except FileNotFoundError:
        st.warning("Sube tu foto (por ejemplo 'natalia.jpg') al directorio principal del proyecto.")

with col2:
    st.markdown(
        """
        ### About me
        I am a student of **EAE Business School** in the subject _Introduction to Programming Languages for Data (IPLD)_.
        
        This web application has been developed as my **final project** for the course.  
        It combines:
        - Python 🐍  
        - Numpy and Pandas for data analysis 📊  
        - Matplotlib for visualizations 📈  
        - Streamlit to deploy everything as a web app 🌐
        """
    )

st.markdown("---")
st.header("Project Overview")

st.markdown(
    """
    This project is divided into three main subprojects, each one implemented in a Jupyter Notebook
    and also integrated in this web application:
    
    1. **Image Cropper**  
       Upload an image and interactively crop it using a simple interface.
    
    2. **Netflix Data Analysis**  
       Explore a dataset of Netflix titles and visualize distributions and trends.
    
    3. **Temperatures Dashboard**  
       Analyze temperature data with flexible filters and time-series visualizations.
    """
)

st.markdown("---")
st.header("Application Sections")

st.markdown(
    """
    You can access the different parts of the project using the menu on the left (Streamlit sidebar):

    - 📷 **Image Cropper** → `01_image_cropper`
    - 🎬 **Netflix Data Analysis** → `02_netflix_data_analysis`
    - 🌡 **Temperatures Dashboard** → `03_temperatures_dashboard`
    """
)

st.markdown("---")

st.info(
    "This app is deployed using **Streamlit Cloud**, and the source code is available in my public GitHub repository."
)
