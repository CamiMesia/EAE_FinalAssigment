# layout.py
import streamlit as st
from PIL import Image

def set_base_style():
    """Aplica el CSS común a todas las páginas."""
    st.markdown("""
    <style>
    /* Fondo degradado del main */
    .main {
        background: radial-gradient(circle at top, #202332 0, #05060a 55%);
        color: #f5f5f5;
    }

    /* Sidebar oscuro */
    [data-testid="stSidebar"] {
        background: #15161c;
        color: #ffffff;
    }

    /* Quitar padding extra arriba */
    .block-container {
        padding-top: 1.5rem;
    }

    /* Tarjeta principal */
    .hero-card {
        background: rgba(10, 10, 15, 0.9);
        border-radius: 24px;
        padding: 32px 42px;
        border: 1px solid rgba(255,255,255,0.07);
        box-shadow: 0 20px 45px rgba(0,0,0,0.55);
    }

    .hero-title {
        font-size: 2.6rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.3rem;
    }
    .hero-title span { color: #ff4d4f; }
    .hero-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #d0d0d0;
    }

    .profile-placeholder {
        width: 220px;
        height: 220px;
        border-radius: 50%;
        border: 5px solid #ff4d4f;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 0.5rem auto;
        color: #ff4d4f;
        font-weight: 700;
        font-size: 22px;
        text-align: center;
    }

    .center { text-align: center; }

    .chip-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.7rem;
        justify-content: center;
        margin-top: 1rem;
    }
    .chip {
        padding: 0.4rem 0.8rem;
        border-radius: 999px;
        border: 1px solid rgba(255,255,255,0.12);
        background: rgba(255,255,255,0.03);
        font-size: 0.88rem;
    }
    </style>
    """, unsafe_allow_html=True)


def render_sidebar():
    """Dibuja el sidebar común a todas las páginas."""
    with st.sidebar:
        # Logo EAE
        try:
            logo = Image.open("eaelogo.png")
            st.image(logo, use_column_width=True)
        except Exception:
            st.markdown("### EAE Business School")
            st.caption("Add eaelogo.png to the project folder.")

        st.markdown("---")
        st.markdown("#### Introduction to Programming Languages for Data")
        st.caption("Final Project – Dec 2025")

        st.markdown("**Author:** Natalia González")   # <- tu nombre
        st.markdown("**Instructor:** Enric Domingo")

        st.markdown("---")
        st.markdown("#### 📂 Navigation")
        st.markdown(
            """
            Use the menu above to switch between pages:

            - 🖼 Image Cropper  
            - 🎬 Netflix Data Analysis  
            - 🌡 Temperatures Dashboard  
            """
        )

        st.markdown("---")
        st.caption("Streamlit multi-page app · EAE IPLD")
