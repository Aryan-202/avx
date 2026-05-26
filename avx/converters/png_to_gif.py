from PIL import Image

def convert_png_to_gif(input_file: str, output_file: str) -> None:
    """Converts a png file to a gif file."""
    with Image.open(input_file) as img:
        if img.mode == 'P':
            img = img.convert('RGB')
        img.save(output_file)
