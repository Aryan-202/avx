from PIL import Image

def convert_tiff_to_png(input_file: str, output_file: str) -> None:
    """Converts a tiff file to a png file."""
    with Image.open(input_file) as img:
        if img.mode == 'P':
            img = img.convert('RGB')
        img.save(output_file)
