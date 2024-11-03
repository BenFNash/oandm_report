import streamlit as st
from graphs.import_export import import_export_bars, import_export_summary 
from PIL import Image
from main import check_password
if not check_password:
    st.stop()

st.title("Executive Summary")
st.header("Dashboard")
import_export_bars()
import_export_summary()
st.header("Overview")
st.write("""
This report has been prepared by BOOM Power Limited in its capacity as the O&M Managers.
Bacup Battery Energy Storage System has been operating since May 2024. Boom Power Ltd are the appointed O&M Contractor.
All issues have been corrected with the Huawei BESS and we are awaiting completion of remedial works to dismiss planning
conditions related to fire water retention, during this period we are conducting hot commissioning to fully test the system.
""")
st.header("Project Overview")

data = {
    "Works Completion ": "24/04/2024",
    "FAC Date": "Not yet awarded",
    "Battery Type": "Lunar 2000 1H1 2.032MWh x 5 batteries",
    "Number of Batteries ": "5",
    "Inverter Type": "40 x Huawei Lunar 2000, 200KTL 1HO",
    "Capacity": "10.16 MWh",
    "Connection Capacity": "8MW"
}

# Displaying data in two columns
for item, value in data.items():
    col1, col2 = st.columns([1, 2])
    col1.write(f"**{item}:**")
    col2.write(value)

st.header("Average Weather Temperature")

# # Load the image
# image_path = "weather_report.png"  # Replace with the path to your PNG file
# st.image(image_path)

st.write("""Average temperature for Bacup Lancashire in September, this can
affect auto consumption through the extra use of aircon and the HVAC
units.
""")
