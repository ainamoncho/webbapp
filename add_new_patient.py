import streamlit as st

MAX_ROWS = 10000

def add_new_patient():
    st.header('Add New Tweet')

    ncolumns = st.session_state.data.shape[1]
    list = []*ncolumns

    with st.form(key='add form', clear_on_submit= True):
        cols = st.columns(ncolumns)
        
        for i in range(ncolumns):
            list.append(st.text_input(st.session_state.data.columns[i]))
    
        if st.form_submit_button('Add Tweet'):
            
            if st.session_state.data.shape[0] == MAX_ROWS:
                st.error('Add tweet limit reached. Cannot add any more tweets')
            else:
                row = st.session_state.data.shape[0]
                st.session_state.data.loc[row] = list
                st.info(f'Tweet: {row} added')

    st.dataframe(st.session_state.data)