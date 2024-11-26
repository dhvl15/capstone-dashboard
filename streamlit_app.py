import streamlit as st

st.set_page_config(page_title='mehul gupta\'s portfolio' ,layout="wide",page_icon='👨‍🔬')

st.sidebar.markdown(info['Stackoverflow_flair'],unsafe_allow_html=True)

st.header('My Debut book on Generative AI is out !!')
st.info("""LangChain in your Pocket: Beginner's Guide to Building Generative AI Applications using LLMs""")

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
