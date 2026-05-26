import markdown

def convert_md_to_html(input_file: str, output_file: str) -> None:
    """Convert md to html."""
    with open(input_file, 'r', encoding='utf-8') as f:
        md_text = f.read()
    html = markdown.markdown(md_text, extensions=['extra', 'codehilite'])
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
