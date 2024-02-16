import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

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

#se eu quero que o meu texto esteja dentro da barra de navegação, incluir "sidebar" entre st e text
st.sidebar.header('Meu texto')

#markdown le o # como um código para dar destaque ao texto que vem a seguir (markdown é uma linguagem)
#st.markdown('# Meu título')

#representa significância para SEO e dá menos destaque ao texto
#st.caption('Minha legenda')

pessoas = [{'Nome': 'Caio', 'Idade':22},
            {'Nome': 'Marcos', 'Idade':33}]
#write é mais genérico, serve para apresentar dados misturados
#st.write("# Pessoas", pessoas)

#exibição de dados
df = pd.DataFrame(
    np.random.rand(10,3),
    columns=['Preço','Taxa de ocupação','Taxa de inadimplência']
)
#diferenças entre table e dataframe. o dataframe permite alterações da tabela pelo usuário ao navegar
#st.dataframe(df)
#st.table(df)

df_pessoas = pd.DataFrame(pessoas)

#elementos gráficos
filtro = st.selectbox('Filtro da tabela', ['Preço', 'Taxa de ocupação', 'Taxa de inadimplência'])
col1, col2, col3 = st.columns(3)

# Adicionando conteúdo às colunas
with col1:
    st.dataframe(df_pessoas)

with col2:
    st.line_chart(df)

with col3:
    st.bar_chart(df_pessoas,x='Nome',y='Idade')

# Exibindo o filtro selecionado
st.write(f'Você selecionou o filtro: {filtro}')

#st.line_chart(df)
#st.bar_chart(df)
#if st.sidebar.button('Exibir opções'):
    #if st.button('Gráfico de linhas'):
        #st.line_chart(df)
    #if st.button('Gráfico de barras'):
        #st.bar_chart(df)

exibir_opcoes = st.sidebar.checkbox('Exibir opções')
if exibir_opcoes:
    opcao_grafico = st.selectbox('Selecione o tipo de gráfico', ['Gráfico de linhas', 'Gráfico de barras', 'Gráfico de pizza'])

    if opcao_grafico == 'Gráfico de linhas':
        st.line_chart(df)
    elif opcao_grafico == 'Gráfico de barras':
        st.bar_chart(df)
    elif opcao_grafico == 'Gráfico de pizza':
            fig = px.scatter(df,x='Preço', y='Taxa de ocupação', title='Gráfico de plotly')
            st.plotly_chart(fig)
