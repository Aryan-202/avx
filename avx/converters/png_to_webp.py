from PIL import Image

def convert_png_to_webp(input_file: str, output_file: str) -> None:
    """Converts a png file to a webp file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """
    with Image.open(input_file) as img:
        if img.mode == 'P':
            img_rgb = img.convert('RGB')
            img_rgb.save(output_file)
            return
        img.save(output_file)
