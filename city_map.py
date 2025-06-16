import folium
from streamlit_folium import st_folium
import streamlit as st

CITY_DATA = {
    "All data": [31.0, -99.0],
    "El sol": [28.7, -100.5],
    "Uvalde": [29.2097, -99.7862],
}

def render_city_map():
    """Render the map and update session state when city is clicked"""
    m = folium.Map(location=[29.5, -99.5], zoom_start=6)

    for city, coords in CITY_DATA.items():
        style = {
            "color": "green" if city == "All data" else "blue",
            "fill_color": "green" if city == "All data" else "blue"
        }

        folium.CircleMarker(
            location=coords,
            radius=8,
            color=style["color"],
            fill=True,
            fill_color=style["fill_color"],
            fill_opacity=0.9,
            popup=f"Active: {city}",
            tooltip=city,
        ).add_to(m)

    map_data = st_folium(m, width=700, height=500)
    popup_text = map_data["last_object_clicked"]["popup"]
    city = popup_text.removeprefix("Active: ").strip()

    if st.session_state.get("selected_city") != city:
        st.session_state["selected_city"] = city
        st.rerun()
