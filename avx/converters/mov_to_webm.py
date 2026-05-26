from moviepy.editor import VideoFileClip

def convert_mov_to_webm(input_file: str, output_file: str) -> None:
    """Converts a mov file to a webm file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, logger=None)
    clip.close()
