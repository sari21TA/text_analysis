import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 
from mtranslate import translate
import pandas as pd
import os
from textblob import TextBlob
import numpy as np

def add_bg_from_url():
  st.markdown(
    f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1535905496755-26ae35d0ae54?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1887&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         [data-testid="stHeader"] {{
         background-color: rgba(0,0,0,0);
         }}
         [data-testid="stSidebar"] {{
         background-image: url("https://images.unsplash.com/photo-1487528742387-d53d4f12488d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1922&q=80");
         background-size: cover;
         }}
         </style>

         """,
    unsafe_allow_html=True
  )
add_bg_from_url()
#title
st.markdown("<h1 style='text-align: center; color: white;font-size:80px'>Language App</h1>", unsafe_allow_html=True)
st.markdown("")
def main():
    activities=["Extract","Translator","Analysis"]
    choice= st.sidebar.selectbox("Select activities",activities)
    if choice=="Extract":
        #title
        st.markdown("<h1 style='text-align: center; color: white; '>Text Extraction</h1>", unsafe_allow_html=True)

        #subtitle
        # st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit`")

        # st.markdown("")

        #image uploader
        image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])

    
        @st.cache
        def load_model(): 
            reader = ocr.Reader(['mr','en','hi'],model_storage_directory='.')
            return reader 

        reader = load_model() #load model

        if image is not None:

            input_image = Image.open(image) #read image
            st.image(input_image) #display image

            with st.spinner("🤖 AI is at Work! "):
                

                result = reader.readtext(np.array(input_image))

                #empty list for results

                result_text = []
                for text in result:
                    result_text.append(text[1])

                st.write(result_text)
            st.success("Here you go!")
            #st.balloons()
        else:
            st.write("Upload an Image")

    elif choice=="Translator":
        # read language dataset
        df = pd.read_excel('pages/language.xlsx',sheet_name='wiki')
        df.dropna(inplace=True)
        lang = df['name'].to_list()
        langlist=tuple(lang)
        langcode = df['iso'].to_list()

        # create dictionary of language and 2 letter langcode
        lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}

        # layout
        st.markdown("<h1 style='text-align: center; color: white; '>Translation</h1>", unsafe_allow_html=True)
        
        inputtext = st.text_area("INPUT",height=200)

        choice = st.sidebar.radio('SELECT LANGUAGE',langlist)
        # I/O
        if len(inputtext) > 0 :
            try:
                output = translate(inputtext,lang_array[choice])
                st.text_area("TRANSLATED TEXT",output,height=200)
            except Exception as e:
                st.error(e)

    elif choice=="Analysis":
        st.markdown("<h1 style='text-align: center; color: white;'>Analysis</h1>", unsafe_allow_html=True)
        from_sent = st.text_input("Enter a sentence")
        if st.button("Analysis"):
            br = TextBlob(from_sent)
            result=br.sentiment.polarity
            if result==0:
                st.success("This is a Neutral Message")
            elif result>0:
                st.success("This is a Positive Message")  
            else :
                st.success("This is a Negative Message")      



if __name__=="__main__":
    main()

