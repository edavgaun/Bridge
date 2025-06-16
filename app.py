import streamlit as st
from eda_dashboard import render_eda
from lda_viewer import render_lda
from load_data import get_html_file_map

# MUST be the first Streamlit command
st.set_page_config(layout="wide")

# Remove default padding
st.markdown("""
    <style>
        .block-container { padding-top: 1rem; }
    </style>
""", unsafe_allow_html=True)

st.title("Texas City Dashboard Explorer")

# Layout: left = controls, right = content
left_col, right_col = st.columns([1, 2])

# LEFT: controls
with left_col:
    st.subheader("Controls")
    city = st.selectbox("Select a City", ["Houston", "Dallas", "Austin", "San Antonio"])
    view_type = st.radio("Select View", ["EDA", "LDA Analysis"])
    st.session_state['selected_city'] = city
    st.session_state['view_type'] = view_type

# RIGHT: dynamic content
with right_col:
    if st.session_state['view_type'] == "EDA":
        render_eda(st.session_state['selected_city'])
    elif st.session_state['view_type'] == "LDA Analysis":
        file_map = get_html_file_map()
        if not file_map:
            st.warning("No LDA files found in lda_results/")
        else:
            selected_doc = st.selectbox("Select LDA File", list(file_map.keys()))
            render_lda(file_map, selected_doc)
