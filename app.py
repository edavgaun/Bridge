# RIGHT COLUMN — city selected view
with right_col:
    city = st.session_state.get("selected_city", None)

    if city:
        st.subheader(f"Analysis for {city}")

        # View toggle
        view_type = st.radio("Select view:", ["EDA", "LDA Analysis"])

        if view_type == "EDA":
            render_eda(city)

        elif view_type == "LDA Analysis":
            file_map = get_html_file_map()

            # Ensure exact match with display name
            st.write("DEBUG file_map:", file_map)
            st.write("DEBUG city:", city)
            if city in file_map:
                render_lda(file_map, city)
            else:
                st.warning(f"No LDA file found for: {city}")
    else:
        st.info("Click a city on the map to begin.")
