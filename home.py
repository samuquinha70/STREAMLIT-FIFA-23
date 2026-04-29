import streamlit as st
import webbrowser
from data import load_data

load_data()

st.title('FIFA 23 Official Dataset! ⚽')
st.sidebar.markdown('Desenvolvido por Samuel')

btn = st.button('Acesse os dados no Kaggle')
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.subheader('Sobre o conjunto de dados')
st.markdown(
    'O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol '
    'profissionais. O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos dos jogadores, '
    'características físicas, estatísticas de jogo, detalhes de contratos e afiliações a clubes.'
)
st.markdown(
    '**Com mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para analistas, pesquisadores e '
    'entusiastas do futebol interessados em explorar vários aspectos do mundo do futebol, pois permite o estudo de '
    'atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores '
    'e desenvolvimento de jogadores ao longo do tempo.'
)
