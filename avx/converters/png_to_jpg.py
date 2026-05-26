from PIL import Image

def convert_png_to_jpg(input_file: str, output_file: str) -> None:
    """Converts a png file to a jpg file."""
    with Image.open(input_file) as img:
        if img.mode in ('RGBA', 'LA', 'P'):
            bg = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            bg.paste(img, mask=img.split()[3])
            img = bg
        img.save(output_file)
