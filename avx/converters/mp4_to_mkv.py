from moviepy.editor import VideoFileClip

def convert_mp4_to_mkv(input_file: str, output_file: str) -> None:
    """Converts a mp4 file to a mkv file."""
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, logger=None)
    clip.close()
