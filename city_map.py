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
        icon = folium.Icon(
            color="green" if city == "All data" else "blue",
            icon="star" if city == "All data" else "info-sign",
            prefix="fa" if city == "All data" else "glyphicon"
        )
        folium.Marker(
            location=coords,
            tooltip=city,
            popup=f"Active: {city}",
            icon=icon
        ).add_to(m)

    map_data = st_folium(m, width=700, height=500)

    # If user clicked a marker, extract the city
    try:
        popup_text = map_data["last_object_clicked"]["popup"]
        clicked_city = popup_text.removeprefix("Active: ").strip()
    except (TypeError, KeyError):
        clicked_city = None

    if clicked_city:
        if st.session_state.get("selected_city") != clicked_city:
            st.session_state["selected_city"] = clicked_city
            st.rerun()
        else:
            st.write("CLICKED CITY:", clicked_city)
