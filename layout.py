import streamlit as st


def set_base_style():
    """Config global de la app: título, icono y padding."""
    st.set_page_config(
        page_title="Introduction to Programming Languages for Data - Final Project",
        page_icon="📊",
        layout="wide",
    )
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
    """Sidebar común, igual al demo oficial."""
    try:
        st.sidebar.image("eaelogo.png", use_container_width=True)
    except Exception:
        st.sidebar.markdown("### EAE Business School")

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
    st.sidebar.write("The pages of this app are available in the page menu:")

    st.sidebar.markdown(
        """
        - 🖼 Image Cropper  
        - 📺 Netflix Data Analysis  
        - 🌡 Temperatures Dashboard  
        """
    )

    st.sidebar.markdown("---")
    st.sidebar.caption("Streamlit multi-page app · EAE IPLD")
