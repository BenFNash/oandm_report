import streamlit as st
from main import check_password
if not check_password:
    st.stop()

st.title("Issues and Status")
# Add content for Page 3 here

