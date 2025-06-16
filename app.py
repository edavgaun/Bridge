import streamlit as st
from eda_dashboard import render_eda
from lda_viewer import render_lda
from load_data import get_html_file_map
from city_map import render_city_map

st.set_page_config(layout="wide")

st.markdown("""
<style>
.block-container { padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

st.title("Texas City Dashboard Explorer")

left_col, right_col = st.columns([1, 2])

# LEFT: MAP
with left_col:
    st.subheader("Click a City")
    clicked_city = render_city_map()
    if clicked_city:
        st.session_state["selected_city"] = clicked_city

# RIGHT: DASHBOARD
with right_col:
    city = st.session_state.get("selected_city", None)

    if city:
        st.subheader(f"Analysis for {city}")
        view_type = st.radio("Select view:", ["EDA", "LDA Analysis"])

        if view_type == "EDA":
            render_eda(city)
        else:
            file_map = get_html_file_map()
            match = [name for name in file_map if name.lower() == city.lower()]
            if match:
                render_lda(file_map, match[0])
            else:
                st.warning(f"No LDA file found for {city}")
    else:
        st.info("Click a city on the map to begin.")
