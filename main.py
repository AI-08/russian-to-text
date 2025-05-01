import io
import streamlit as st

from transformers import pipeline
from PIL import Image

code[class*="language-"], pre[class*="language-"]
  text-shadow: 0 1px #14161800 !important
  background: #242424 !important
  span.token.operator
    background: none
  span.token.keyword
    color: #866cba

def load_image():
    uploaded_file = st.file_uploader(label='OCRусский - распознай русский текст с изображения')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None


st.title('Выберите изображение для распознавания')
img = load_image()

result = st.button('Распознать текст🪄')
if result:
    captioner = pipeline("image-to-text", "Akajackson/donut_rus")
    text = captioner(img)
    st.write('**Немного магии, и ты получаешь:**')
    st.write(text[0]["generated_text"])
