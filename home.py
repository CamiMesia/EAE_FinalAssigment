import streamlit as st
from PIL import Image

# ---------- CONFIG BÁSICA ----------
st.set_page_config(
    page_title="IPLD Final Project",
    page_icon="👩‍💻",
    layout="wide"
)

# ---------- ESTILOS (CSS) ----------
st.markdown(
    """
    <style>
    /* Fondo oscuro y texto claro en el área principal */
    .main {
        background-color: #101014;
        color: white;
    }
    /* Sidebar oscuro */
    [data-testid="stSidebar"] {
        background-color: #15151b;
    }
    /* Centrar texto de algunos bloques */
    .centered {
        text-align: center;
    }
    /* Imagen de perfil redonda */
    .profile-img {
        width: 260px;
        height: 260px;
        border-radius: 50%;
        object-fit: cover;
        border: 6px solid #ff0000;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- SIDEBAR ----------
with st.sidebar:
    # Logo EAE
    try:
        logo = Image.open("eae_logo.png")   # <-- cambia el nombre si tu archivo se llama distinto
        st.image(logo, use_column_width=True)
    except Exception:
        st.warning("Añade el archivo 'eae_logo.png' en la carpeta del proyecto.")

    st.markdown("## Introduction to Programming<br>Languages for Data", unsafe_allow_html=True)

    st.markdown("*Final Project - Dec 2025*")  # Cambia el año si quieres que ponga 2023

    st.markdown("**Author:** Natalia González")      # <-- pon aquí tu nombre
    st.markdown("**Instructor:** Enric Domingo")     # <-- nombre del profesor

# ---------- CONTENIDO PRINCIPAL ----------
st.markdown("<h1 class='centered'>My name is Natalia González</h1>", unsafe_allow_html=True)

# Imagen de perfil en círculo
try:
    profile = Image.open("profile.jpg")   # <-- cambia si tu foto tiene otro nombre
    st.markdown("<div class='centered'>", unsafe_allow_html=True)
    st.image(profile, use_column_width=False, width=260, caption="")  # la clase CSS hace el círculo
    st.markdown("</div>", unsafe_allow_html=True)
except Exception:
    # Si no encuentra la imagen, muestra un círculo con texto como en la demo
    st.markdown(
        """
        <div class='centered'>
            <div style="
                width:260px;
                height:260px;
                border-radius:50%;
                border:6px solid #ff0000;
                display:flex;
                align-items:center;
                justify-content:center;
                margin:auto;
                color:#ff0000;
                font-weight:bold;
                font-size:26px;
                text-align:center;
                ">
                Your<br>Profile<br>Image
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <p class="centered" style="margin-top:30px; font-style:italic;">
    Short description and/or Studies or Description
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown(
    """
    <p class="centered">
    This web application is my final project for the subject 
    <strong>Introduction to Programming Languages for Data</strong> at 
    <strong>EAE Business School</strong>.
    </p>
    """,
    unsafe_allow_html=True
)

