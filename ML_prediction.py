import streamlit as st
import numpy as np
import pickle
import xgboost
import pandas as pd
import shap
from streamlit_shap import st_shap

def ML_prediction():
    st.header('Machine Learning Prediction')
    
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
    
    # Predictiong ICU for all patients
    prediction = model.predict(df)

    # Creating the explainer and calculating shap_values object for the patients dataset
    explainer = shap.TreeExplainer(model)
    shap_values = explainer(df)

    # After user choses the patient, we display the predicted ICU of this patient
    patient = st.slider('Select a patient', 0, st.session_state.data.shape[0]-1)
    if st.button('Predict ICU'): 
        if prediction[patient] == 0:
            st.write('The patient did not require ICU attendance')
        if prediction[patient] == 1:
            st.write('The patient required ICU attendance')

        # Local interpretation of the prediction using SHAP 
        shap.initjs()
        st.subheader('Waterfall plot')
        st_shap(shap.plots.waterfall(shap_values[patient]))
        
        st.subheader('Force plot')
        st_shap(shap.force_plot(explainer.expected_value, shap_values.values[patient], features=df.iloc[patient], link='logit'))
        
        st.subheader('Decision plot')
        st_shap(shap.decision_plot(explainer.expected_value, shap_values.values[patient], features=df.iloc[patient]))