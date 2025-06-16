import streamlit as st
from eda_dashboard import render_eda
from lda_viewer import render_lda
from load_data import get_html_file_map
from city_map import render_city_map

# Set layout before anything else
st.set_page_config(layout="wide")

# Optional: minimal spacing
st.markdown("""
<style>
.block-container { padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

# App title
st.title("Texas City Dashboard Explorer")

# Create layout
left_col, right_col = st.columns([1, 2])

# LEFT: Render map (handles click + sets session state + reruns)
with left_col:
    st.subheader("Click a City")
    render_city_map()

# RIGHT: Get city from session state (not from function return)
with right_col:
    city = st.session_state.get("selected_city", None)
    if city:
        st.write(f"You selected: **{city}**")
    else:
        st.info("No city selected yet.")
