import streamlit as st
from graphs.import_export import import_export_bars_with_av
from graphs.cycles import warranty_vs_actual_cycles, warrant_vs_actual_cycles_table
from main import check_password
if not check_password:
    st.stop()


st.title("Site Performance")
st.header("Site Performance, Import and Export and Availability")
import_export_bars_with_av()

st.write("""
         The above chart is representative of September’s Import, Export & Availability. The days showing little to no Import &
Export are due to changing of Optimiser. Availability down by 1.2% (17/09/2024) can be because of O&M works and BESS
being put into sleep mode briefly. No trading is being conducted during this period of changing Optimiser and Hot
Commissioning.
         """)

st.header("Monthly Operation Report")
st.write("During the month of September the current optimiser (Statkraft) did not conduct any trades.")

warrant_vs_actual_cycles_table()
warranty_vs_actual_cycles()
st.write("""
         These are the cumulative cycles for the previous 8 months; the Huawei warranty dictates we are allowed 2000 for
48 months from 02/2024. This averages 41.66 per month. We are currently below our warranty amount.
         """)
