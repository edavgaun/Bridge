
import streamlit as st
import pandas as pd
import pydeck as pdk

# Sample data for Texas cities
city_data = pd.DataFrame({
    'City': ['Houston', 'Dallas', 'Austin', 'San Antonio'],
    'Latitude': [29.7604, 32.7767, 30.2672, 29.4241],
    'Longitude': [-95.3698, -96.7970, -97.7431, -98.4936]
})

st.set_page_config(layout="wide")
st.title("Texas City Dashboard Explorer")

left_col, right_col = st.columns([1, 2])

if 'selected_city' not in st.session_state:
    st.session_state['selected_city'] = None

with left_col:
    st.subheader("Select a city:")
    layer = pdk.Layer(
        'ScatterplotLayer',
        data=city_data,
        get_position='[Longitude, Latitude]',
        get_radius=70000,
        get_fill_color='[200, 30, 0, 160]',
        pickable=True
    )
    view_state = pdk.ViewState(latitude=31.0, longitude=-99.0, zoom=5.5)
    r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{City}"})
    st.pydeck_chart(r)

    selected_city = st.selectbox("Or choose from list:", city_data['City'].tolist())
    st.session_state['selected_city'] = selected_city

with right_col:
    st.subheader(f"Dashboard for {st.session_state['selected_city']}")

    if st.session_state['selected_city'] == 'Houston':
        st.write("Population: 2.3M")
        st.line_chart([10, 20, 30])
    elif st.session_state['selected_city'] == 'Dallas':
        st.write("Population: 1.3M")
        st.bar_chart([5, 25, 15])
    elif st.session_state['selected_city'] == 'Austin':
        st.write("Population: 950K")
        st.area_chart([15, 30, 10])
    elif st.session_state['selected_city'] == 'San Antonio':
        st.write("Population: 1.5M")
        st.line_chart([25, 10, 5])
