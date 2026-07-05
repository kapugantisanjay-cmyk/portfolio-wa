import streamlit as st

st.set_page_config(page_title="portfolio",layout="wide")

col1,col2=st.columns([1,2],border=False)

with col1:
    st.image("asserts/image.jpeg",width=200,caption="KapugantiSanjay")
    
with col2:
    st.title("KapugantiSanjay")
    st.subheader("Linux|Selenuim|Tosca|Mainframes|Python")
    st.write("This is my portfolio Linux Expert,Selenium Expert,Manual Testing,Azure and Python Expert")
    st.download_button("resume",open("asserts/resume.pdf","rb"),file_name="resume.pdf")

    st.divider()

    c1,c2,c3=st.columns(3)

with c1:
    st.metric("Experience","8+")

with c2:
    st.metric("Projects","100+")

with c3:
    st.metric("Companies worked","4+")