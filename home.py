import streamlit as st
from PIL import Image
from layout import set_base_style, render_sidebar
set_base_style()
render_sidebar()
st.markdown("""
<style>

.hero-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    margin-top: 0rem;
    margin-bottom: -0.5rem;
}
.hero-title span {
    color: #ff4d4d;
}

.hero-sub {
    text-align:center;
    font-size: 1.1rem;
    color: #e6e6e6;
    margin-bottom: 2rem;
}

.profile-circle {
    width: 260px;
    height: 260px;
    border-radius: 50%;
    border: 6px solid #ff4d4d;
    display:flex;
    align-items:center;
    justify-content:center;
    margin: auto;
    margin-bottom: 1rem;
    font-weight:700;
    color:#ff4d4d;
    font-size:22px;
}

.section-description {
    text-align:center;
    font-size: 1.0rem;
    color: #cccccc;
    margin-top: 0.7rem;
}

.chips-row {
    display:flex;
    justify-content:center;
    flex-wrap:wrap;
    gap:0.7rem;
    margin-top:1.5rem;
}
.chip {
    padding:0.5rem 1rem;
    border-radius:999px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.15);
    font-size:0.9rem;
    color:#ffffff;
}

.footer-text {
    text-align:center;
    font-size:0.9rem;
    color:#cccccc;
    margin-top:2rem;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 class="hero-title">👋 Hi, my name is <span>Natalia González</span></h1>
<p class="hero-sub">🎓 Final Project • Introduction to Programming Languages for Data • EAE Business School</p>
""", unsafe_allow_html=True)
col_l, col_center, col_r = st.columns([1,1,1])

with col_center:
    loaded_img = False
    for f in ["profile.png", "profile.jpg", "profile.jpeg"]:
        try:
            img = Image.open(f)
            st.image(img, width=260)
            loaded_img = True
            break
        except:
            pass

    if not loaded_img:
        st.markdown('<div class="profile-circle">📸<br>Your<br>Profile<br>Image</div>', unsafe_allow_html=True)

    st.markdown('<p class="section-description">💻 Data enthusiast • Python & Pandas • Streamlit Web Apps</p>', unsafe_allow_html=True)

st.markdown("""
<p class="section-description" style="max-width:900px; margin:auto;">
This interactive web app is my final project for <strong>EAE Business School</strong>.  
It combines <strong>data analysis, notebooks, image processing, dashboards</strong> and UI components built in Streamlit.
</p>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class="chips-row">
    <div class="chip">🖼 Image Cropper · basic image processing</div>
    <div class="chip">📊 Netflix Data Analysis · exploratory analytics</div>
    <div class="chip">🌡 Temperatures Dashboard · time series & filters</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div class="footer-text">
✨ Use the menu on the left to navigate through the project sections.<br>
🧭 Start exploring from the sidebar.
</div>
""", unsafe_allow_html=True)
