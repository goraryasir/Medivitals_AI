import streamlit as st
from vitals import get_vitals
from chatbot import chat_with_bot

st.set_page_config(page_title="MediVitals AI", layout="wide")

st.title("🧠 MediVitals AI – Smart Contactless Health Companion")

tab1, tab2 = st.tabs(["🩺 Vitals Estimation", "💬 Symptom Checker"])

with tab1:
    st.header("Estimate Health Vitals (Camera Required)")
    get_vitals()

with tab2:
    st.header("Chat with AI Doctor")
    user_input = st.text_input("Describe your symptoms:")
    if user_input:
        response = chat_with_bot(user_input)
        st.success(response)
