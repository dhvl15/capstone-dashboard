import streamlit as st

st.title("IE 7945 - Capstone Project")
tab1, tab2, tab3, tab4 = st.tabs(["HOME", "EDA", "NER", "RESULTS"])

with tab1:
    st.image("https://media.zenfs.com/en/newsfile_64/bc71d8ce103e8469e0c829ce0c349ccd", width=200)
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_whP2XVgmkIVOyrIuAb5D4PtUaMOpq4R-Yw&s", width=200)

with tab2:
    st.header("Exploratory Data Analysis")
    
    # Power BI embed URL
    powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=15c71f3d-94a4-4168-b7c7-4893a83b4149&autoAuth=true&ctid=a8eec281-aaa3-4dae-ac9b-9a398b9215e7"

    # Display the Power BI report using an iframe
    st.components.v1.html(
        f"""
        <iframe width="100%" height="800" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>
        """,
        height=800,
    )
    #st.components.html("https://app.powerbi.com/links/SDbL2VLHaD?ctid=a8eec281-aaa3-4dae-ac9b-9a398b9215e7&pbi_source=linkShare/embed", width = 500, height = 200, scrolling = True)
    

with tab3:
    st.header("Named Entity Recognition")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab4:
    st.header("Results")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
