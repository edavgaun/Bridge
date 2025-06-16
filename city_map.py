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
    popup_value = None
    
    if isinstance(map_data, dict) and "last_object_clicked" in map_data:
        popup = map_data["last_object_clicked"].get("popup")
        if popup:
            popup_value = popup[8:]
            clicked_city = popup_value
            st.write("POPUP VALUE:", popup_value)
        else:
            st.write("Click detected but no popup content.")
    else:
        st.write("MAP DATA is empty or no click registered.")
    
    if (clicked_city and 
        ("selected_city" not in st.session_state or st.session_state["selected_city"] != clicked_city)
        ):
        st.session_state["selected_city"] = clicked_city
        st.write("CLICKED CITY:", clicked_city)
        st.rerun()
