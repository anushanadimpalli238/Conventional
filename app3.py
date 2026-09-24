import streamlit as st
import ollama 
st.header("AI CHATBOT") 
st.subheader("Welcome! to the Conversation")
you=st.text_input("YOU:")
if you:
    if you.lower()=="exit":
        st.write("Good bye.") 
    else:
        response=ollama.chat(
            model="llama3.2",
            messages=[{"role":"user",
                       "content":you}]
        )  
        st.write("Bot:",response["message"]["content"])   
