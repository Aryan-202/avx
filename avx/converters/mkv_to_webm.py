from moviepy.editor import VideoFileClip

def convert_mkv_to_webm(input_file: str, output_file: str) -> None:
    """Converts a mkv file to a webm file."""
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, logger=None)
    clip.close()
