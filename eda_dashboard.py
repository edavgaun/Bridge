import streamlit as st

def render_eda(city):
    st.subheader(f"EDA Dashboard for {city}")

    demo_data = {
        'All data': [12, 18, 24],
        'El sol': [8, 16, 12],
        'Uvalde': [14, 22, 20]
    }

    st.write(f"Population estimate for {city}:")
    st.line_chart(demo_data.get(city, [0, 0, 0]))
