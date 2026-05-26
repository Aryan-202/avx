from moviepy.editor import VideoFileClip

def convert_mkv_to_avi(input_file: str, output_file: str) -> None:
    """Converts a mkv file to a avi file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, logger=None)
    clip.close()
