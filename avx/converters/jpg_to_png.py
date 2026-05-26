from PIL import Image

def convert_jpg_to_png(input_file: str, output_file: str) -> None:
    """Converts a jpg file to a png file."""
    with Image.open(input_file) as img:
        if img.mode == 'P':
            img = img.convert('RGB')
        img.save(output_file)
