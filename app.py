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

# RIGHT: Dashboard view
with right_col:
    city = st.session_state.get("selected_city", None)
    st.write("DEBUG file_map:", file_map)
    st.write("DEBUG city:", city)

    if city:
        st.subheader(f"Analysis for {city}")

        # Show radio button to switch views
        view_type = st.radio("Select view:", ["EDA", "LDA Analysis"])

        if view_type == "EDA":
            render_eda(city)

        elif view_type == "LDA Analysis":
            file_map = get_html_file_map()

            # Match by city name inside the HTML filenames
            match = [key for key in file_map if city.lower() in key.lower()]

            if match:
                render_lda(file_map, match[0])  # display the matching HTML
            else:
                st.warning(f"No LDA file found for {city}")
    else:
        st.info("Click a city on the map to begin.")

