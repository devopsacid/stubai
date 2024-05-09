import streamlit as st
import qa as qa_glib


st.set_page_config(page_title="STU AI TEAM") #HTML title
st.title("STU AI TEAM") #page title



if 'vector_index' not in st.session_state: 
    with st.spinner("Indexing document..."): 
        st.session_state.vector_index = qa_glib.get_index()



input_text = st.text_area("Input text", label_visibility="collapsed")
go_button = st.button("Go", type="primary")



if go_button:
    
    with st.spinner("Working..."):
        response_content = qa_glib.get_rag_response(index=st.session_state.vector_index, question=input_text)
        
        st.write(response_content)