import os
import streamlit as st

def render_lda(file_map, selected_name, folder="lda_results"):
    file_path = os.path.join(folder, file_map[selected_name])
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    st.components.v1.html(html, height=700, scrolling=True)
