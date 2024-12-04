import streamlit as st
import spacy_streamlit
import os
import spacy
from spacy_streamlit import load_model
import pandas as pd
from streamlit_d3graph import d3graph
from PIL import Image
from pathlib import Path
import base64
from st_social_media_links import SocialMediaIcons
from wordcloud import WordCloud

st.set_page_config(layout="wide")
st.title("IE 7945 - Capstone Project")
st.subheader("From Data Overload to Clear Insights : Tackling Vulnerabilities with AI")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["HOME", "EDA", "NER", "RESULTS", "TEAM"])

def resize_to_height(image_path, target_height):
    img = Image.open(image_path)
    aspect_ratio = img.width / img.height
    new_width = int(target_height * aspect_ratio)
    resized_img = img.resize((new_width, target_height), Image.ANTIALIAS)  # Smooth resizing
    return resized_img

# Team data
team_members = [
    {
        "name": "Dhaval Jariwala",
        "email": "jariwala.dh@northeastern.edu",
        "linkedin": "https://www.linkedin.com/in/dhavaljariwala15",
        "image_path": "p1.png",  # Replace with the actual path to Alice's image
    },
    {
        "name": "Vaishnavi Sadul",
        "email": "sadul.v@northestern.edu",
        "linkedin": "https://www.linkedin.com/in/bobjohnson",
        "image_path": "p3.png",  # Replace with the actual path to Bob's image
    },
    {
        "name": "Yihua Cai",
        "email": "cai.yihu@northeastern.edu",
        "linkedin": "https://www.linkedin.com/in/yihua-cai/",
        "image_path": "p4.jpeg",  # Replace with the actual path to Catherine's image
    },
    {
        "name": "Yuze Li",
        "email": "li.yuze3@northeastern.edu",
        "linkedin": "https://www.linkedin.com/",
        "image_path": "p5.png",  # Replace with the actual path to David's image
    },
]


with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(
            "https://media.zenfs.com/en/newsfile_64/bc71d8ce103e8469e0c829ce0c349ccd",
            width=300,
        )
    
    with col2:
        st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_whP2XVgmkIVOyrIuAb5D4PtUaMOpq4R-Yw&s",
            width=300,
        )

    st.text('''Understanding cybersecurity data often feels overwhelming due to the sheer complexity of the information. This paper presents a streamlined solution leveraging artificial intelligence (AI) to transform data from the National Vulnerability Database (NVD) into actionable insights. 
            Key contributions include a custom Named Entity Recognition (NER) pipeline tailored to cybersecurity datasets, an interactive dashboard for visualizing trends, and a knowledge graph for revealing hidden relationships among vulnerabilities. 
            Our approach enhances the ability to identify and manage risks efficiently, significantly outperforming generic AI models in identifying critical patterns.''')

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
    

with tab3:
   with tab3:
    st.header("Named Entity Recognition")

    file = open('text2.txt')
    text = file.read()
    file.close()
    nlp = spacy.load("custom_ner_model")
    doc = nlp(text)

    colors = {
        "VENDOR": "#ffca80",
        "PRODUCT": "#ff80bf",
        "FEATURE": "#ff9580",
        "ACTOR": "#80ffea",
        "EXPLOIT" : "#ffff80",
        "MODULE" : "#8aff80",
        "VULNERABILITY NAME" : "#9580ff"  
    }

    spacy_streamlit.visualize_ner(
        doc,
        labels=['VENDOR', 'PRODUCT', 'FEATURE', 'ACTOR', 'EXPLOIT', 'MODULE', 'VULNERABILITY NAME'],
        show_table=False,
        title="Manual visualization of Tags",
        colors=colors,
        #manual=True
    )

def load_html_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            st.error(f"File not found: {file_path}")
            return None
        
with tab4:

    st.header("Results")
   
    # url = "pages/knowledge_graph22.html"

    # with open(url, 'r') as file:
    #     html_content = file.read()
    #     st.components.v1.html(html_content, height=800)
   
    
    
    # Path to your HTML file
    url = "pages/knowledge_graph22.html"
    
    # Show a loading spinner while reading the file
    with st.spinner("Loading results..."):
        html_content = load_html_file(url)

    # If the file was successfully loaded, display the content
    if html_content:
        st.components.v1.html(html_content, height=800)

        col1, col2 = st.columns(2)
    
    with col1:
        st.image(
            "output1.png",
            #width=300,
        )
    
    with col2:
        st.image(
            "output2.png",
            #width=300,
        )

with tab5:
    st.header("Meet the Team")
    
    cols = st.columns(4)  # Create four columns for the team members
    target_height = 300  # Set target height for images

    # Style for circular images
    circular_style = """
    <style>
        .circular-img {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            margin-bottom: 10px;
        }
    </style>
    """

    # Inject the CSS style
    st.markdown(circular_style, unsafe_allow_html=True)

    # Display team members
    for i, member in enumerate(team_members):
        with cols[i]:
            image_path = Path(member["image_path"])
            if image_path.is_file():
                # Read the image and encode it in base64
                with open(image_path, "rb") as img_file:
                    base64_img = base64.b64encode(img_file.read()).decode("utf-8")
                
                # Display circular image using HTML
                st.markdown(
                    f"""
                    <img src="data:image/png;base64,{base64_img}" 
                         class="circular-img" 
                         alt="{member['name']}">
                    """,
                    unsafe_allow_html=True,
                )
            else:
                st.write(f"Image for {member['name']} not found!")

            # Display name, email, and LinkedIn link
            st.markdown(
                f"""
                <h2 style="font-weight: bold; font-size: 30px;">{member['name']}</h2>
                """,
                unsafe_allow_html=True,
            )
            
            st.markdown(
                f"""
                <div style="display: flex; align-items: center; gap: 10px;">
                    <a href="{member['linkedin']}" target="_blank">
                        <img src="https://img.icons8.com/?size=100&id=xuvGCOXi8Wyg&format=png&color=000000" alt="LinkedIn" style="width: 24px; height: 24px; color:blue">
                    </a>
                    <a href="mailto:{member['email']}" target="_blank">
                        <img src="https://img.icons8.com/?size=100&id=dFXkWptwH7Wz&format=png&color=000000" alt="Email" style="width: 24px; height: 24px;">
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.text("")
    st.text("")
    st.text("")
    st.text("Supervised by : Prof. Qurat-ul-Ain Azim")