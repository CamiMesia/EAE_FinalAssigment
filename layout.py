import streamlit as st


def set_base_style():
    st.set_page_config(
        page_title="EAE IPLD · Final Project",
        page_icon="📊",
        layout="wide",
    )

    # Estilos generales
    st.markdown(
        """
        <style>
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 4rem;
            padding-right: 4rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar():

    st.sidebar.image("eaelogo.png")
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        **Introduction to Programming  
        Languages for Data**

        *Final Project – Dec 2025*

        **Author:** Natalia González  

        **Instructor:** Enric Domingo
        """,
    )

    st.sidebar.markdown("---")
    st.sidebar.subheader("📂 Navigation")
    st.sidebar.write("Use the buttons below to switch between pages:")
    st.sidebar.page_link("home.py", label="👋 Home")
    st.sidebar.page_link("pages/01_image_cropper.py", label="🖼 Image Cropper")
    st.sidebar.page_link("pages/02_netflix_data_analysis.py", label="📺 Netflix Data Analysis")
    st.sidebar.page_link("pages/03_temperatures_dashboard.py", label="🌡 Temperatures Dashboard")

    st.sidebar.markdown("---")
    st.sidebar.caption("Streamlit multi-page app · EAE IPLD")

