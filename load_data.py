import os

def get_html_file_map(folder="lda_results"):
    """Returns dict: {display_name: filename}"""
    html_files = [f for f in os.listdir(folder) if f.endswith(".html")]
    display_names = [
        f.replace("lda_visualization_", "").replace(".html", "")
        for f in html_files
    ]
    return dict(zip(display_names, html_files))
