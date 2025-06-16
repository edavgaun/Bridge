import folium
from streamlit_folium import st_folium
import streamlit as st
import json

CITY_DATA = {
    "All data": [31.0, -99.0],
    "El sol": [28.7, -100.5],
    "Uvalde": [29.2097, -99.7862],
}

def render_city_map():
    """Render the map and update session state when city is clicked"""
    m = folium.Map(location=[29.5, -99.5], zoom_start=6)

    for city, coords in CITY_DATA.items():
        if city == "All data":
            icon = folium.Icon(color="green", icon="star", prefix="fa")
        else:
            icon = folium.Icon(color="blue", icon="info-sign", prefix="glyphicon")

        folium.Marker(
            location=coords,
            tooltip=city,
            popup='Active: {}'.format(city),
            icon=icon
        ).add_to(m)

    map_data = st_folium(m, width=400, height=500)
    
    clicked_city = None
    if map_data and map_data.get("last_object_clicked"):
        popup_value = map_data["last_object_clicked"].get("popup")
        st.write("POPUP VALUE:", popup_value)  # And this
        if popup_value and popup_value.startswith("Active: "):
            clicked_city = popup_value[8:]
    
    if (
        clicked_city
        and (
            "selected_city" not in st.session_state
            or st.session_state["selected_city"] != clicked_city
        )
    ):
        st.session_state["selected_city"] = clicked_city
        st.write("CLICKED CITY:", clicked_city)
        st.rerun()
    else:
        st.write("MAP DATA DEBUG:", json.dumps(map_data, indent=2))


