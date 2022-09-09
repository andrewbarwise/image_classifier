import warnings
import streamlit as st
from PIL import Image
from resnet101 import predict

warnings.simplefilter('ignore')

st.set_option('deprecation.showfileUploaderEncoding', False)
st.write("")

file_up = st.file_uploader('Upload an image', type="jpg")

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption='Uploaded image.', use_column_width=True)
    st.write("")
    st.write("Uploading...")
    labels = predict(file_up)

try:
    for ii in labels:
        st.write("Prediction: ", ii[0], ", Score: ", ii[1])
except NameError:
    st.write(" ")