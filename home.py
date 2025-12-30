import streamlit as st
from PIL import Image
import streamlit as st
from layout import set_base_style, render_sidebar
set_base_style()
render_sidebar()
st.set_page_config(
    page_title="IPLD Final Project",
    page_icon="👩‍💻",
    layout="wide"
)

layout.set_base_style()
layout.render_sidebar()
st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">Hi, my name is <span>Natalia González</span></div>
        <div class="hero-subtitle">
            Final Project · Introduction to Programming Languages for Data · EAE Business School
        </div>
    """,
    unsafe_allow_html=True
)

col_left, col_mid, col_right = st.columns([1, 1.2, 1])

with col_mid:
    try:
        profile = Image.open("profile.jpg")
        st.image(profile, width=220, caption="", output_format="PNG")
    except Exception:
        st.markdown(
            """
            <div class="profile-placeholder">
                Your<br>Profile<br>Image
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown(
        """
        <p class="center" style="margin-top:0.3rem; color:#d0d0d0; font-size:0.95rem;">
        Data enthusiast · Python & Pandas · Streamlit Web Apps
        </p>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <p class="center" style="margin-top:1.0rem; font-size:1.0rem; color:#f0f0f0;">
    This web application is my final project for the course 
    <strong>Introduction to Programming Languages for Data (IPLD)</strong>.
    It combines Jupyter Notebooks, data analysis and interactive visualizations
    deployed as a Streamlit app.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="chip-row">
        <div class="chip">🖼 Image Cropper · basic image processing</div>
        <div class="chip">🎬 Netflix Data Analysis · exploratory data analysis</div>
        <div class="chip">🌡 Temperatures Dashboard · time series & filters</div>
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown("### 📚 Project Overview")

st.markdown(
    """
| Section | Description | Technologies |
|--------|-------------|--------------|
| 🖼 **Image Cropper** | Upload, crop and download images interactively. | PIL, Streamlit widgets |
| 🎬 **Netflix Data Analysis** | Explore a Netflix titles dataset with filters and plots. | Pandas, Matplotlib |
| 🌡 **Temperatures Dashboard** | Analyze temperature evolution by city and date range. | Pandas, Matplotlib, time series |
    """,
    unsafe_allow_html=True
)

st.success("✔️ Home page ready. Use the sidebar to navigate to each subproject.")

