import streamlit as st
import folium
from streamlit_folium import st_folium

# Hardcoded Texas city coordinates
CITY_DATA = {
    "Houston": [29.7604, -95.3698],
    "Dallas": [32.7767, -96.7970],
    "Austin": [30.2672, -97.7431],
    "San Antonio": [29.4241, -98.4936],
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
        ).add_to(m)

    # Render the map
    map_data = st_folium(m, width=400, height=500)

    # Return clicked city (from popup)
    if map_data and map_data.get("last_object_clicked"):
        return map_data["last_object_clicked"].get("popup")

    return None
