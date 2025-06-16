import streamlit as st
from streamlit_leaflet import st_leaflet
from streamlit_leaflet.js_utils import bind
from streamlit_leaflet.components import Map, Marker

CITY_DATA = {
    "All data": [31.0, -99.0],
    "El sol": [28.7, -100.5],
    "Uvalde": [29.2097, -99.7862],
}

def render_city_map():
    markers = []

    for city, coords in CITY_DATA.items():
        markers.append(
            Marker(
                position=coords,
                event_handlers={"click": bind("marker_click", city)},
                options={"title": city}
            )
        )

    result = st_leaflet(
        Map(center=[29.5, -99.5], zoom=6, children=markers, height="500px"),
        key="city_map"
    )

    clicked_city = result.get("marker_click")

    if clicked_city and st.session_state.get("selected_city") != clicked_city:
        st.session_state["selected_city"] = clicked_city
        st.rerun()
