import folium
from streamlit_folium import st_folium

CITY_DATA = {
    "All data": [31.0, -99.0],
    "El sol": [28.7, -100.5],
    "Uvalde": [29.2097, -99.7862],
}

def render_city_map():
    """Render the map and return clicked city name (if any)"""
    m = folium.Map(location=[29.5, -99.5], zoom_start=6)

    for city, coords in CITY_DATA.items():
        if city == "All data":
            icon = folium.Icon(color="green", icon="star", prefix="fa")  # distinct icon
        else:
            icon = folium.Icon(color="blue", icon="info-sign", prefix="glyphicon")  # normal icon

        folium.Marker(
            location=coords,
            popup=city,
            tooltip=city,
            icon=icon
        ).add_to(m)

    map_data = st_folium(m, width=400, height=500)

    if map_data and map_data.get("last_object_clicked"):
        return map_data["last_object_clicked"].get("popup")

    return None
