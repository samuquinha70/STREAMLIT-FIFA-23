import pandas as pd
import streamlit as st
from datetime import datetime


def load_data():
    if 'data' not in st.session_state:
        df = pd.read_csv('dataseats/CLEAN_FIFA23_official_data.csv', index_col=0)
        df = df[df['Contract Valid Until'] >= datetime.today().year]
        df = df[df['Value(£)'] > 0]
        df = df.sort_values(by='Overall', ascending=False)
        st.session_state['data'] = df
