import streamlit as st
from eda_dashboard import render_eda
from lda_viewer import render_lda
from load_data import get_html_file_map
from city_map import render_city_map

# Must be first Streamlit command
st.set_page_config(layout="wide")

# Optional: remove extra top padding
st.markdown("""
<style>
.block-container { padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

# App title
st.title("Texas City Dashboard Explorer")

# Two-column layout: map on left, dashboard on right
left_col, right_col = st.columns([1, 2])

# LEFT: Render clickable map and capture selected city
with left_col:
    st.subheader("Click a City")
    city = render_city_map()  # Returns selected city via session_state

# RIGHT: Show EDA or LDA analysis for selected city
with right_col:
    if city:
        st.subheader(f"Analysis for {city}")

        # Radio button to switch views
        view_type = st.radio("Select view:", ["EDA", "LDA Analysis"])

        if view_type == "EDA":
            render_eda(city)

        elif view_type == "LDA Analysis":
            file_map = get_html_file_map()
            match = [name for name in file_map if name.lower() == city.lower()]

            if match:
                render_lda(file_map, match[0])
            else:
                st.warning(f"No LDA file found for {city}")

    else:
        st.info("Click a city on the map to begin.")
