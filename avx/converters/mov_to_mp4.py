from moviepy.editor import VideoFileClip

def convert_mov_to_mp4(input_file: str, output_file: str) -> None:
    """Converts a mov file to a mp4 file."""
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, logger=None)
    clip.close()
