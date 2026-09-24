import streamlit as st
import ollama 
st.title("AI CHATBOT")
st.write("Welcome to our new chatbot")
prompt=st.text_input("Enter your prompt")
if st.button("click"):
    response=ollama.chat(
        model="llama3.2",
        messages=[{"role":"user",
                   "content":prompt}]) 
    st.write(response["message"]["content"])  
    
 
    