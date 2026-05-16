from PIL import Image


def convert_jpg_to_png(input_file: str, output_file: str) -> None:
    """
    Converts a JPG file to a PNG using Pillow.
    
    Args:
        input_file: Path to the source .jpg file.
        output_file: Path where the .png should be saved.
    """
    with Image.open(input_file) as img:
        img.save(output_file)
