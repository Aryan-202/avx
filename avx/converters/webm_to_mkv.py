from moviepy.editor import VideoFileClip

def convert_webm_to_mkv(input_file: str, output_file: str) -> None:
    """Converts a webm file to a mkv file."""
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, logger=None)
    clip.close()
