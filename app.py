import streamlit as st
from gtts import gTTS
def text_to_speech(text, language='en'):
    tts = gTTS  (text=text, lang=language, slow=False)
    tts.save("output.mp3")
    st.audio("output.mp3")
#tampilan Ui  
st.title ("Liverpool")
st.caption ("Just a Random Code")
st.toast ('By Jonathan')
st.write ('Use it Wisely')
text = st.text_input("Input Your Text Mate :)")
language = st.selectbox("Select Your Language", ("en", "id", "es", "zh-CN", "pt"))
if st.button ("play"):
    text_to_speech(text, language)