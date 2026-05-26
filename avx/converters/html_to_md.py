from markdownify import markdownify

def convert_html_to_md(input_file: str, output_file: str) -> None:
    """Convert html to md."""
    with open(input_file, 'r', encoding='utf-8') as f:
        html_text = f.read()
    md = markdownify(html_text)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md)
