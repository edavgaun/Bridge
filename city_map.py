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
        color = "blue" if city == "All data" else "red"
        folium.CircleMarker(
            location=coords,
            radius=5,
            color=color,
            fill=True,
            fill_opacity=0.6,
            tooltip=city
        ).add_to(m)

    map_data = st_folium(m, width=700, height=500)

    click = map_data.get("last_clicked")

    if click:
        lat, lng = int(click["lat"]), int(click["lng"])
        for city, (city_lat, city_lng) in CITY_DATA.items():
            if int(city_lat) == lat and int(city_lng) == lng:
                st.session_state["selected_city"] = city
                break
