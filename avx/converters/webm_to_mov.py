from moviepy.editor import VideoFileClip

def convert_webm_to_mov(input_file: str, output_file: str) -> None:
    """Converts a webm file to a mov file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, logger=None)
    clip.close()
