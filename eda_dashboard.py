import streamlit as st

def render_eda(city):
    st.subheader(f"EDA Dashboard for {city}")

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
