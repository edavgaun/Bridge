import os

def get_html_files(folder="lda_results"):
    html_files = [f for f in os.listdir(folder) if f.endswith(".html")]
    clean_names = [f.replace("lda_visualization_", "").replace(".html", "") for f in html_files]
    return dict(zip(clean_names, html_files))
