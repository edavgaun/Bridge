import streamlit as st

def render_eda(city):
    st.subheader(f"EDA Dashboard for {city}")

    demo_data = {
        'Houston': [10, 20, 30],
        'Dallas': [5, 25, 15],
        'Austin': [15, 30, 10],
        'San Antonio': [25, 10, 5]
    }

    st.write(f"Population estimate for {city}:")
    st.line_chart(demo_data.get(city, [0, 0, 0]))
