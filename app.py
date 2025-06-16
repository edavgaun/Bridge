import streamlit as st
from eda_dashboard import render_eda
from lda_viewer import render_lda
from load_data import get_html_file_map

st.set_page_config(layout="wide")

# Remove padding if needed
st.markdown("""
<style>
.block-container { padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

# Title
st.title("Texas City Dashboard Explorer")

# Define columns (map/city selector left, dashboard right)
left_col, right_col = st.columns([1, 2])

# LEFT: City selector only
with left_col:
    st.subheader("Select a City")
    city = st.selectbox("City", ["Houston", "Dallas", "Austin", "San Antonio"])
    st.session_state["selected_city"] = city

# RIGHT: Radio and dashboard
with right_col:
    st.subheader("BRIDGE Analysis")

    # Radio button placed in right panel (correct placement)
    view_type = st.radio("Select view:", ["EDA", "LDA Analysis"])
    st.session_state["view_type"] = view_type

    if view_type == "EDA":
        render_eda(city)
    else:
        file_map = get_html_file_map()
        if not file_map:
            st.warning("No LDA visualizations available.")
        else:
            selected_file = st.selectbox("Select LDA File", list(file_map.keys()))
            render_lda(file_map, selected_file)
