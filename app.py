import streamlit as st
from eda_dashboard import render_eda
from lda_viewer import render_lda
from load_data import get_html_file_map
from city_map import render_city_map

# Set layout first
if "initialized" not in st.session_state:
    st.set_page_config(layout="wide")
    st.session_state["initialized"] = True

# Optional: Remove default top padding
st.markdown("""
<style>
.block-container { padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

# Title
st.title("Texas City Dashboard Explorer")

# Create layout
left_col, right_col = st.columns([1, 2])

# LEFT: map interaction
with left_col:
    st.subheader("Click a City")
    render_city_map()

# RIGHT: show view based on selected city
with right_col:
    city = st.session_state.get("selected_city", None)

    if city:
        st.subheader(f"Analysis for {city}")

        view_type = st.radio("Select view:", ["EDA", "LDA Analysis"])

        if view_type == "EDA":
            render_eda(city)

        elif view_type == "LDA Analysis":
            file_map = get_html_file_map()
            
            # Use exact match for city names from LDA filenames
            if city in file_map:
                render_lda(file_map, city)
            else:
                st.warning(f"No LDA file found for: {city}")

    else:
        st.info("Click a city on the map to begin.")
