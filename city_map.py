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

    for city, coords in CITY_DATA.items():
        folium.Marker(
            location=coords,
            tooltip=city,
            popup=f"Active: {city}"
        ).add_to(m)

    map_data = st_folium(m, width=700, height=500)

    try:
        click = map_data["last_clicked"]
        clicked_lat = int(click["lat"])
        clicked_lng = int(click["lng"])

        for city, (lat, lng) in CITY_DATA.items():
            if int(lat) == clicked_lat and int(lng) == clicked_lng:
                st.session_state["selected_city"] = city
                st.rerun()
    except:
        pass
