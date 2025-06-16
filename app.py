# Import necessary libraries
import streamlit as st      # Main Streamlit app framework
import pandas as pd         # For working with tabular data
import pydeck as pdk        # For interactive map visualization
import folium
from streamlit_folium import st_folium

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
left_col, right_col = st.columns([1.5, 2])  # Width ratio: 1 for map, 2 for dashboard

# ----------------------------------------------------------
# Initialize session state to remember selected city
# ----------------------------------------------------------
if 'selected_city' not in st.session_state:
    st.session_state['selected_city'] = None  # Initialize with no city selected

# -----------------------
# LEFT PANEL: Folium Map
# -----------------------
with left_col:
    st.subheader("Click a marker or choose from dropdown")

    # Create Folium map
    m = folium.Map(location=[31.0, -99.0], zoom_start=6)

    # Add city markers
    for i, row in city_data.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['City'],
            tooltip=row['City'],
        ).add_to(m)

    # Display map
    map_data = st_folium(m, width=400, height=500)

    # Detect click from marker popup or fallback to dropdown
    clicked_city = None
    if map_data.get("last_object_clicked"):
        clicked_city = map_data["last_object_clicked"].get("popup")

    # Fallback if nothing clicked
    if not clicked_city:
        clicked_city = st.selectbox("Or choose from list:", city_data['City'].tolist())

    # Save to session state
    st.session_state['selected_city'] = clicked_city


# ----------------------------------------------------------
# RIGHT COLUMN: Dynamic Dashboard Based on City
# ----------------------------------------------------------
with right_col:
    city = st.session_state['selected_city']
    st.subheader(f"BRIDGE Analysis")

    # Radio buttons for dashboard type
    view_type = st.radio("Select view:", ["Exploratory Data Analysis (EDA)", 
                                          "Latent Dirichlet Allocation (LDA) Analysis"])

    if view_type == "Exploratory Data Analysis (EDA)":
        # Simple EDA charts per city (dummy data for now)
        if city == 'Houston':
            st.write("Population: 2.3M")
            st.line_chart([10, 20, 30])
        elif city == 'Dallas':
            st.write("Population: 1.3M")
            st.bar_chart([5, 25, 15])
        elif city == 'Austin':
            st.write("Population: 950K")
            st.area_chart([15, 30, 10])
        elif city == 'San Antonio':
            st.write("Population: 1.5M")
            st.line_chart([25, 10, 5])

    elif view_type == "Latent Dirichlet Allocation (LDA) Analysis":
        # Placeholder for topic modeling results
        st.markdown("### LDA Topic Modeling Results")

        # Replace with your real topic modeling output (static for now)
        st.markdown(f"""
        **Top Topics for {city}:**
        - Topic 1: _education, training, workforce_
        - Topic 2: _technology, manufacturing, automation_
        - Topic 3: _policy, funding, infrastructure_
        """)

        # Optional: show LDA word clouds, tables, etc.
        st.info("This section could show word clouds, topic distributions, or interactive visualizations.")
