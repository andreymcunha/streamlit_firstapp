import streamlit as st
import google.generativeai as gen_ai
import os
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px

load_dotenv()


st.set_page_config(page_title="Teste 01",
                   page_icon=":brain:",
                   layout="wide"
                   )
st.write("Bem-vindo")

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

#função para traduzir "roles" entre Gemini-pro e Streamlit
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
    


#inicializar o chat (session) se já não foi inicializado
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

#mostrar o histórico de mensagem
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)


#user message
user_prompt = st.chat_input("Faça uma pergunta")
if user_prompt:
    #Adiciona o a mensagem no chat e mostra ela
    st.chat_message('user').markdown(user_prompt)

    #Envia a mensagem para o Gemini e pega a resposta
    gemini_response=(st.session_state.chat_session.send_message(user_prompt))
                     

    #mostra a resposta do gemini
    with st.chat_message("assistante"):
        st.markdown(gemini_response.text)


        
