from PIL import Image

def convert_bmp_to_jpeg(input_file: str, output_file: str) -> None:
    """Converts a bmp file to a jpeg file."""
    with Image.open(input_file) as img:
        if img.mode in ('RGBA', 'LA', 'P'):
            bg = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            bg.paste(img, mask=img.split()[3])
            img = bg
        img.save(output_file)
