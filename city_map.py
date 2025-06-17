import streamlit as st
import folium
from streamlit_folium import st_folium

CITY_DATA = {
    "All data": [31.0, -99.0],
    "El sol": [28.7, -100.5],
    "Uvalde": [29.2097, -99.7862],
}

def render_city_map():
    m = folium.Map(location=[29.5, -99.5], zoom_start=6)
    m.add_child(folium.LatLngPopup())

    # FIXED: Use default folium icons to avoid broken image links
    for city, coords in CITY_DATA.items():
        folium.Marker(
            location=coords,
            tooltip=city,
            popup=city,  # keep popup simple for clarity
            icon=folium.Icon(color="blue" if city != "All data" else "green")
        ).add_to(m)

    # Render map
    map_data = st_folium(m, width=700, height=500)

    # Show the exact last_clicked object on screen
    last_click = map_data.get("last_clicked")
    st.write("🧭 last_clicked data:", last_click)
