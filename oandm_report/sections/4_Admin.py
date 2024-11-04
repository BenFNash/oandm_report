import streamlit as st
st.header("Admin - Edit Report Captions")

# Editable captions for each chart
st.subheader("Edit Captions")
    
with st.form("caption_form"):
    st.session_state["captions"]["overview"] = st.text_area(
        "Caption for Overview", st.session_state["captions"]["overview"]
    )
    st.session_state["captions"]["avg_weather"] = st.text_area(
        "Caption for Average weather", st.session_state["captions"]["avg_weather"]
    )
    st.session_state["captions"]["import_export"] = st.text_area(
        "Caption for Import Export chart", st.session_state["captions"]["import_export"]
    )
    st.session_state["captions"]["operations_report"] = st.text_area(
        "Caption for Operations report", st.session_state["captions"]["operations_report"]
    )
    st.session_state["captions"]["cumul_cycles"] = st.text_area(
        "Caption for Cycles chart", st.session_state["captions"]["cumul_cycles"]
    )

    # Submit button for form
    submitted = st.form_submit_button("Save Captions")
    if submitted:
        st.success("Captions updated successfully!")
