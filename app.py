import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from add_new_patient import add_new_patient
from ML_prediction import ML_prediction
from global_interpretation import global_interpretation

st.set_page_config(
    page_title='HOSPITAL',
    page_icon='🏥',
    layout='wide',
    initial_sidebar_state='expanded',
)

st.title('🏥 HOSPITAL')

with st.sidebar:
    page = option_menu('Main Menu', ['Home', 'Add New Text', 'Machine Learning Prediction', 'Global Interpretation'], 
        icons=['house', 'bag-plus', 'arrow-bar-up', 'bar-chart-line'], menu_icon="cast", default_index=1,
        styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "red", "font-size": "20px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "grey"},
    })

#data = pd.read_csv('stage_1_balanced.csv', sep=';')
data = pd.read_csv('test.tsv', sep='\t')

if 'data' not in st.session_state:
    st.session_state.data=data


if page == 'Home':
    if st.checkbox('Display data'):
        st.write(st.session_state.data)

if page == 'Add New Patient':
    add_new_patient()

if page == 'Machine Learning Prediction':
    ML_prediction()

if page == 'Global Interpretation':
    global_interpretation()