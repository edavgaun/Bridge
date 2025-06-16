import streamlit as st
import folium
from streamlit_folium import st_folium

# Hardcoded Texas city coordinates
CITY_DATA = {
    "All data": [31.0, -99.0],         # placeholder central TX
    "El sol": [28.7, -100.5],          # approximate location
    "Uvalde": [29.2097, -99.7862],     # actual Uvalde, TX
}

def render_city_map():
    """Render the Folium map and return the clicked city (if any)"""

    # Create map centered on Texas
    m = folium.Map(location=[31.0, -99.0], zoom_start=6)

    # Add markers
    for city, coords in CITY_DATA.items():
        folium.Marker(
        location=coords,
        popup=city,
        tooltip=city,
        icon=folium.Icon(icon="info-sign", prefix="glyphicon")
        ).add_to(m)


    # Render the map
    map_data = st_folium(m, width=400, height=500)

    # Return clicked city (from popup)
    if map_data and map_data.get("last_object_clicked"):
        return map_data["last_object_clicked"].get("popup")

    return None
