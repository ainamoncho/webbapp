import streamlit as st
import numpy as np
import pickle
import xgboost
import pandas as pd
#import shap
#from streamlit_shap import st_shap

def global_interpretation():
    st.header('Global Interpretation')
    
    # Reading pickle file
    with open('finalized_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Managing patients data as needed
    df = st.session_state.data
    try:
        df = df.drop(['ICU'], axis=1)
        df = df.drop(['Unnamed: 0'], axis=1)
    except:
        pass
    
    # Creating the explainer and calculating shap_values object for the patients dataset
    #explainer = shap.TreeExplainer(model)
    #shap_values = explainer(df)

    # Global interpretation of the prediction using SHAP
    '''
    shap.initjs()
    
    st.subheader('Summary plot')
    st_shap(shap.summary_plot(shap_values, df, plot_size=0.2))
    
    st.subheader('Bar plot')
    st_shap(shap.plots.bar(shap_values, max_display=20))
    
    st.subheader('Scatter plot')
    listcol = ['Choose a feature']
    listcol = listcol + list(df)
    column_name = st.selectbox('', listcol)
    if column_name != 'Choose a feature':
        st_shap(shap.plots.scatter(shap_values[:, column_name]))
    '''