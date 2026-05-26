from PIL import Image

def convert_gif_to_webp(input_file: str, output_file: str) -> None:
    """Converts a gif file to a webp file."""
    with Image.open(input_file) as img:
        if img.mode == 'P':
            img = img.convert('RGB')
        img.save(output_file)
