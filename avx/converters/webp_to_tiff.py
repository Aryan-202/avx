from PIL import Image

def convert_webp_to_tiff(input_file: str, output_file: str) -> None:
    """Converts a webp file to a tiff file."""
    with Image.open(input_file) as img:
        if img.mode == 'P':
            img = img.convert('RGB')
        img.save(output_file)
