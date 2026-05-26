from moviepy.editor import VideoFileClip

def convert_avi_to_webm(input_file: str, output_file: str) -> None:
    """Converts a avi file to a webm file."""
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, logger=None)
    clip.close()
