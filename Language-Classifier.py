import pickle
import streamlit as st

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


infile = open('ClassPick', 'rb')
lr = pickle.load(infile)
infile.close()

st.sidebar.success("Choose")

st.title('Language Classification')
st.write('This app can classify upto 17 Languages  (English, French, Spanish, Hindi, Portugeese, Italian, Russian, '
             'Swedish, Malayalam, Dutch, Arabic, Turkish, German, Tamil, Danish, Kannada, Greek)')

title = st.text_input("Enter the Language to Classify")
if st.button('Classify'):
     st.success('The Language is '+lr.predict([title])[0])