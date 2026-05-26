from PIL import Image

def convert_bmp_to_jpeg(input_file: str, output_file: str) -> None:
    """Converts a bmp file to a jpeg file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """
    with Image.open(input_file) as img:
        if img.mode in ('RGBA', 'LA', 'P'):
            bg = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img_rgba = img.convert('RGBA')
                bg.paste(img_rgba, mask=img_rgba.split()[3])
                bg.save(output_file)
                return
            bg.paste(img, mask=img.split()[3])
            bg.save(output_file)
            return
        img.save(output_file)
