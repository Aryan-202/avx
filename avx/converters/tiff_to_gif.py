from PIL import Image

def convert_tiff_to_gif(input_file: str, output_file: str) -> None:
    """Converts a tiff file to a gif file."""
    with Image.open(input_file) as img:
        if img.mode == 'P':
            img = img.convert('RGB')
        img.save(output_file)
