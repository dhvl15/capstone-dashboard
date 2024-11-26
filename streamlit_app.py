import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(["HOME", "EDA", "NER", "RESULTS"])

with tab1:
    st.header("IE7945 - Capstone roject")
    st.image("https://media.zenfs.com/en/newsfile_64/bc71d8ce103e8469e0c829ce0c349ccd", width=200)
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_whP2XVgmkIVOyrIuAb5D4PtUaMOpq4R-Yw&s", width=200)



with tab2:
    st.header("Exploratory Data Analysis")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    
with tab3:
    st.header("Named Entity Recognition")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab4:
    st.header("Results")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
