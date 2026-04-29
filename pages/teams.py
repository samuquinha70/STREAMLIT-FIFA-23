import base64
import requests
import streamlit as st


# 1. Definida a função que estava faltando
def load_image_64(url):
    try:
        response = requests.get(url)
        return f"data:image/png;base64,{base64.b64encode(response.content).decode()}"
    except Exception as e:
        return url


def preprocess_row(url):
    if isinstance(url, str) and url.startswith("http"):
        return load_image_64(url)
    return url


st.set_page_config(
    page_title='Players',
    page_icon='🏃',
    layout='wide'
)

# 2. Corrigido de parênteses () para colchetes []
df_data = st.session_state['data']

clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Clube', clubes)

df_filtered = df_data[(df_data['Club'] == club)].set_index('Name')

st.image(df_filtered.iloc[0]['Club Logo'])
# Adicionado um espaço após as hashtags para o Markdown reconhecer o título corretamente
st.markdown(f'## {club}')

columns = [
    'Age', 'Photo', 'Flag', 'Overall', 'Value(£)', 'Wage(£)', 'Joined',
    'Height(cm.)', 'Weight(lbs.)',
    'Contract Valid Until', 'Release Clause(£)',
]

# 3. Manipulação de dados movida para FORA do st.dataframe
df_filtered["Photo"] = df_filtered["Photo"].apply(preprocess_row)
df_filtered["Flag"] = df_filtered["Flag"].apply(preprocess_row)
df_filtered["Club Logo"] = df_filtered["Club Logo"].apply(preprocess_row)

# 4. st.dataframe agora contém apenas o dicionário válido no column_config
st.dataframe(
    df_filtered[columns],
    column_config={
        'Overall': st.column_config.ProgressColumn(
            'Overall', format='%d', min_value=0, max_value=100
        ),
        'Wage(€)': st.column_config.ProgressColumn(
            'Weekly Wage', format='£%f', min_value=0, max_value=df_filtered['Wage(£)'].max()
        )
    }
)
