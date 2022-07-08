import streamlit as st
imoort joblib
model = joblib.load('spam-ham')
st.title('spam-ham CLASSIFIER')
ip = st.text_input('Enter your message')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
