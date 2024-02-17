import streamlit as st

#Textos
#faz os elementos ocuparem todo o espaço da tela. OBS.: Set_page_config só pode ser chamado uma vez por página de app e precisa ser a primeira linha de comando no script
st.set_page_config(page_title='teste app',
                   layout='wide',
                   page_icon='random')
st.header('Meu Dashboard')
st.text('Meu texto')

#uso de session state, Here's a simple app that counts the number of times the page has been run. Every time you click the button, the script will rerun.
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1
if st.session_state.counter == 10:
     st.header(f"Acho que agora já deu, né? {st.session_state.counter} é bastante, da um F5 aí")
else:
    st.header(f"Essa página rodou {st.session_state.counter} vezes.")
st.button("Clica aqui rapidão")

