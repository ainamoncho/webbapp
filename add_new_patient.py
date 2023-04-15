import streamlit as st

MAX_ROWS = 10000

def add_new_patient():
    st.header('Add New Patient')

    ncolumns = st.session_state.data.shape[1]
    list = []*ncolumns

    with st.form(key='add form', clear_on_submit= True):
        cols = st.columns(ncolumns)
        
        for i in range(ncolumns):
            list.append(st.number_input(st.session_state.data.columns[i]))
    
        if st.form_submit_button('Add Patient'):
            
            if st.session_state.data.shape[0] == MAX_ROWS:
                st.error('Add patient limit reached. Cannot add any more patients')
            else:
                row = st.session_state.data.shape[0]
                st.session_state.data.loc[row] = list
                st.info(f'Patient: {row} added')

    st.dataframe(st.session_state.data)
