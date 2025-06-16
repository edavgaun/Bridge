import os
import streamlit as st

def render_lda(selected_name, name_to_file, folder="lda_results"):
    st.markdown(f"### LDA Topic Modeling: {selected_name}")
    file_path = os.path.join(folder, name_to_file[selected_name])
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    st.components.v1.html(html, height=700, scrolling=True)
