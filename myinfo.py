import streamlit as st
from PIL import Image

st.title('About Me')
mypic = Image.open('myface.jpg')
st.image(mypic,width=300,caption="Me")
