import streamlit as st
import hmac
import streamlit as st


if "captions" not in st.session_state:
    st.session_state["captions"] = {
        "overview": """This report has been prepared by BOOM Power Limited in its capacity as the O&M Managers. Bacup Battery Energy Storage System has been operating since May 2024. Boom Power Ltd are the appointed O&M Contractor. All issues have been corrected with the Huawei BESS and we are awaiting completion of remedial works to dismiss planning conditions related to fire water retention, during this period we are conducting hot commissioning to fully test the system.""",
        "avg_weather": """Average temperature for Bacup Lancashire in September, this can affect auto consumption through the extra use of aircon and the HVAC units.""",
        "import_export": """The above chart is representative of September’s Import, Export & Availability. The days showing little to no Import & Export are due to changing of Optimiser. Availability down by 1.2% (17/09/2024) can be because of O&M works and BESS being put into sleep mode briefly. No trading is being conducted during this period of changing Optimiser and Hot Commissioning.""",
        "operations_report": """During the month of September the current optimiser (Statkraft) did not conduct any trades.""",
        "cumul_cycles": """These are the cumulative cycles for the previous 8 months; the Huawei warranty dictates we are allowed 2000 for 48 months from 02/2024. This averages 41.66 per month. We are currently below our warranty amount."""
    }


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False

if not check_password():
    st.stop()

if check_password():
    pg = st.navigation([
        st.Page("sections/1_Executive_Summary.py"),
        st.Page("sections/2_Site_Performance.py"),
        st.Page("sections/3_Issues_and_Status.py"),
        st.Page("sections/4_Admin.py"),
    ])
    pg.run()


