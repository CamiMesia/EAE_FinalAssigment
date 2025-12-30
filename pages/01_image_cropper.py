import streamlit as st
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Image Cropper", page_icon="🖼")

st.title("🖼 Image Cropper")

st.write(
    """
    Upload an image and use the sliders to crop it.  
    This page corresponds to the **Image Cropper** subproject of the IPLD final assignment.
    """
)

# Subir imagen
uploaded_file = st.file_uploader("Upload an image file", type=["png", "jpg", "jpeg"])

if uploaded_file is None:
    st.info("Please upload an image to start.")
    st.stop()

# Abrir imagen
image = Image.open(uploaded_file).convert("RGB")
st.subheader("Original image")
st.image(image, use_column_width=True)

width, height = image.size

st.markdown("### Crop settings")

col1, col2 = st.columns(2)

with col1:
    left = st.slider("Left (x1)", 0, width - 1, 0)
    top = st.slider("Top (y1)", 0, height - 1, 0)

with col2:
    right = st.slider("Right (x2)", left + 1, width, width)
    bottom = st.slider("Bottom (y2)", top + 1, height, height)

# Recorte
cropped_image = image.crop((left, top, right, bottom))

st.subheader("Cropped image")
st.image(cropped_image, use_column_width=True)

# Datos de info
st.write(f"**Original size:** {width} x {height}")
st.write(f"**Cropped size:** {cropped_image.size[0]} x {cropped_image.size[1]}")

# Descargar imagen recortada
buffer = BytesIO()
cropped_image.save(buffer, format="PNG")
buffer.seek(0)

st.download_button(
    label="Download cropped image",
    data=buffer,
    file_name="cropped_image.png",
    mime="image/png"
)
