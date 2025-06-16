# Import necessary libraries
import streamlit as st      # Main Streamlit app framework
import pandas as pd         # For working with tabular data
import pydeck as pdk        # For interactive map visualization

# ----------------------------------------------------------
# Create a sample dataset of Texas cities with coordinates
# ----------------------------------------------------------
city_data = pd.DataFrame({
    'City': ['Houston', 'Dallas', 'Austin', 'San Antonio'],
    'Latitude': [29.7604, 32.7767, 30.2672, 29.4241],
    'Longitude': [-95.3698, -96.7970, -97.7431, -98.4936]
})

# ----------------------------------------------------------
# Set up Streamlit page layout and title
# ----------------------------------------------------------
st.set_page_config(layout="wide")  # Use wide layout for 2-column view
st.title("Texas City Dashboard Explorer")  # App title at the top

# ----------------------------------------------------------
# Create two side-by-side columns (map on left, dashboard on right)
# ----------------------------------------------------------
left_col, right_col = st.columns([1, 2])  # Width ratio: 1 for map, 2 for dashboard

# ----------------------------------------------------------
# Initialize session state to remember selected city
# ----------------------------------------------------------
if 'selected_city' not in st.session_state:
    st.session_state['selected_city'] = None  # Initialize with no city selected

# ----------------------------------------------------------
# LEFT COLUMN: Interactive Texas Map
# ----------------------------------------------------------
with left_col:
    st.subheader("Select a city:")

    # Create a PyDeck scatterplot layer to show city markers
    layer = pdk.Layer(
        'ScatterplotLayer',  # Type of visualization
        data=city_data,  # Data to use (lat/lon of cities)
        get_position='[Longitude, Latitude]',  # Coordinates
        get_radius=70000,  # Size of each circle on map
        get_fill_color='[200, 30, 0, 160]',  # Color of the markers (red)
        pickable=True  # Enable tooltips when hovering
    )

    # Set the initial view of the map (centered over Texas)
    view_state = pdk.ViewState(
        latitude=31.0,
        longitude=-99.0,
        zoom=5.5
    )

    # Combine map layer and view into a Deck object
    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{City}"}  # Show city name when hovered
    )

    # Display the interactive map
    st.pydeck_chart(r)

    # Provide a dropdown menu to select a city manually
    selected_city = st.selectbox("Or choose from list:", city_data['City'].tolist())

    # Save selected city to session state for use in right panel
    st.session_state['selected_city'] = selected_city

# ----------------------------------------------------------
# RIGHT COLUMN: Dynamic Dashboard Based on City
# ----------------------------------------------------------
with right_col:
    # Show the city name in the panel header
    st.subheader(f"Dashboard for {st.session_state['selected_city']}")

    # Display a simple chart depending on which city is selected
    if st.session_state['selected_city'] == 'Houston':
        st.write("Population: 2.3M")
        st.line_chart([10, 20, 30])  # Placeholder line chart

    elif st.session_state['selected_city'] == 'Dallas':
        st.write("Population: 1.3M")
        st.bar_chart([5, 25, 15])  # Placeholder bar chart

    elif st.session_state['selected_city'] == 'Austin':
        st.write("Population: 950K")
        st.area_chart([15, 30, 10])  # Placeholder area chart

    elif st.session_state['selected_city'] == 'San Antonio':
        st.write("Population: 1.5M")
        st.line_chart([25, 10, 5])  # Another line chart
